from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options
options = Options()
options.binary_location = "/home/me/firefox-esr/firefox/firefox"  # <- Adjust if your username/path differs

# Path to geckodriver (system-installed or snap-installed one)
service = Service("/snap/bin/geckodriver")

# Launch browser
driver = webdriver.Firefox(service=service, options=options)

# Open a page
driver.get("https://opportunity.ini.rw/")
time.sleep(3)

# Print the page title
print("Page title:", driver.title)

# Close the browser
driver.quit()
