from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint

# Initialize the Selenium WebDriver (using Chrome in this case)
driver = webdriver.Chrome()  # Or replace with webdriver.Firefox() for Firefox

def get_all_forms(url):
    """Returns all form tags found on a web page's 'url'"""
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load completely (optional, for JavaScript-heavy pages)
    driver.implicitly_wait(5)
    
    # Get the page source after the JavaScript has executed
    page_source = driver.page_source
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")
    return soup.find_all("form")
    
def get_form_details(form):
    """Returns the HTML details of a form, including action, method, and list of form controls (inputs, etc.)"""
    details = {}
    # Get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # Get the form method (POST, GET, DELETE, etc.)
    method = form.attrs.get("method", "get").lower()
    # Get all form inputs
    inputs = []
    
    # Process input tags
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    
    # Process select tags
    for select in form.find_all("select"):
        select_name = select.attrs.get("name")
        select_type = "select"
        select_options = []
        select_default_value = ""
        for select_option in select.find_all("option"):
            option_value = select_option.attrs.get("value")
            if option_value:
                select_options.append(option_value)
                if select_option.attrs.get("selected"):
                    select_default_value = option_value
        if not select_default_value and select_options:
            select_default_value = select_options[0]
        inputs.append({"type": select_type, "name": select_name, "values": select_options, "value": select_default_value})

    # Process textarea tags
    for textarea in form.find_all("textarea"):
        textarea_name = textarea.attrs.get("name")
        textarea_type = "textarea"
        textarea_value = textarea.text
        inputs.append({"type": textarea_type, "name": textarea_name, "value": textarea_value})
        
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    
    return details

if __name__ == "__main__":
    # Define the URL to be scraped
    url = "https://www.amazon.com/"
    forms = get_all_forms(url)
    
    if not forms:
        print("No forms found on the page.")
    else:
        for i, form in enumerate(forms, start=1):
            form_details = get_form_details(form)
            print("="*50, f"form #{i}", "="*50)
            pprint(form_details)
    
    # Close the browser window
    driver.quit()
