from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class SecurityInfoScraper:
    def __init__(self, browser='chrome'):
        self.browser = browser
        self.driver = self.setup_browser()
        
    def setup_browser(self):
        """Set up the WebDriver for Chrome or Brave."""
        chrome_options = Options()
        
        if self.browser == 'brave':
            # Correct path to Brave browser using raw string
            chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application"
        else:
            # Correct path to Chrome browser using raw string
            chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application"
        
        # Set up the Chrome WebDriver manager to automatically manage drivers
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver
    
    def scrape_security_info(self, url):
        """Scrape security information from a given URL."""
        self.driver.get(url)
        time.sleep(2)
        
        # Example: Find and scrape security-related headlines
        headlines = self.driver.find_elements(By.CSS_SELECTOR, 'h2')  # Adjust CSS selector to target specific headlines

        # Print and return the headlines
        for headline in headlines:
            print(headline.text)

        return [headline.text for headline in headlines]

    def close_browser(self):
        """Close the browser."""
        self.driver.quit()


if __name__ == "__main__":
    url = "https://accounts.ecitizen.go.ke/en"  # Replace with the target website for security info

    # Choose either 'chrome' or 'brave' as the browser
    scraper = SecurityInfoScraper(browser='brave')  # Use 'chrome' for Chrome browser
    
    # Scrape security information
    security_info = scraper.scrape_security_info(url)

    # Close the browser
    scraper.close_browser()
