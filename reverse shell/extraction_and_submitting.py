from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pprint import pprint

# Initialize an HTTP session
session = HTMLSession()

def get_all_forms(url):
    """Returns all form tags found on a web page's 'url'"""
    # GET request
    res = session.get(url)
    # For JavaScript driven websites, uncomment the line below
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
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
        # Get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # Get name attribute
        input_name = input_tag.attrs.get("name")
        # Get the default value of that input tag
        input_value = input_tag.attrs.get("value", "")
        # Add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    
    # Process select tags
    for select in form.find_all("select"):
        # Get the name attribute
        select_name = select.attrs.get("name")
        # Set the type as select
        select_type = "select"
        select_options = []
        # The default select value
        select_default_value = ""
        # Iterate over options and get the value of each
        for select_option in select.find_all("option"):
            # Get the option value used to submit the form
            option_value = select_option.attrs.get("value")
            if option_value:
                select_options.append(option_value)
                if select_option.attrs.get("selected"):
                    # If 'selected' attribute is set, set this option as default    
                    select_default_value = option_value
        if not select_default_value and select_options:
            # If the default is not set, and there are options, take the first option as default
            select_default_value = select_options[0]
        # Add the select to the inputs list
        inputs.append({"type": select_type, "name": select_name, "values": select_options, "value": select_default_value})

    # Process textarea tags
    for textarea in form.find_all("textarea"):
        # Get the name attribute
        textarea_name = textarea.attrs.get("name")
        # Set the type as textarea
        textarea_type = "textarea"
        # Get the textarea value
        textarea_value = textarea.text
        # Add the textarea to the inputs list
        inputs.append({"type": textarea_type, "name": textarea_name, "value": textarea_value})
        
    # Put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    
    return details

if __name__ == "__main__":
    import sys
    # Get URL from the command line
    url = sys.argv[1]
    # Get all form tags
    forms = get_all_forms(url)
    # Iterate over forms
    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        print("="*50, f"form #{i}", "="*50)
        pprint(form_details)
