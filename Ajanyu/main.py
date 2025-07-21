import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Set up Firefox options
options = Options()
options.binary_location = os.getenv("FIREFOX_BIN", "/home/me/firefox-esr/firefox/firefox")

# Set up GeckoDriver service
geckodriver_path = os.getenv("GECKODRIVER_PATH", "/snap/bin/geckodriver")
service = Service(geckodriver_path)

driver = None  # So we can reference it in finally

try:
    # Launch browser
    driver = webdriver.Firefox(service=service, options=options)

    # Open a page
    driver.get("https://opportunity.ini.rw/")
    time.sleep(3)

    # Print the page title
    print("Page title:", driver.title)

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    if driver:
        driver.quit()
        print("✅ Browser closed.")
