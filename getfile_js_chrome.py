from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_options.binary_location = r'C:\ProgramData\Anaconda3\Scripts\chromedriver.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://www.duo.com")
print("Chrome Browser Initialized in Headless Mode")
driver.quit()
print("Driver Exited")