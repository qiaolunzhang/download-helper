from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('http://www.cs.cornell.edu/courses/cs1112/2017fa/#templates/syllabus?section=lectures')

sleep(5)

html  = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(html)

browser.close()

