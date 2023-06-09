import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# Set up WebDriver options
options = webdriver.ChromeOptions()

# Generate a fake user agent
ua = UserAgent()
user_agent = ua.random

# Set the fake user agent
options.add_argument(f"user-agent={user_agent}")

# Create a WebDriver instance using WebDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Visit the URL
url = "https://www.dextools.io/app/en/fantom/pair-explorer/0xb5512e3fa8304d33cdae4a40c21f1d3f70eba45a"
driver.get(url)

# Sleep for 10 seconds
time.sleep(10)

# Get the page text
page_text = driver.page_source

# Print the page text
print(page_text)

# Close the WebDriver instance
driver.quit()
