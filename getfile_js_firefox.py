# firefox driver: geckodriver.exe
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

# firefox_options.binary_location = r'C:\ProgramData\Anaconda3\Scripts\geckodriver.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=r'C:\ProgramData\Anaconda3\Scripts\geckodriver.exe')

time.sleep(3)
driver.get("http://www.cs.cornell.edu/courses/cs1112/2017fa/#templates/syllabus?section=lectures")
r = driver.page_source
print(r)
soup = BeautifulSoup(r, 'lxml')
for link in soup.find_all('a'):
    print(link.get('href'))
print("Firefox Browser Initialized in Headless Mode")
driver.quit()
print("Driver Exited")