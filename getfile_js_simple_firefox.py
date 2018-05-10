import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from time import sleep


def get_ref(start_url):
    try:
        browser = webdriver.Firefox()
        browser.get(start_url)
        sleep(5)
        text = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    except:
        print("failed")
        return

    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
    print('******************************************')
    print('******************************************')
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)
        try:
            file_name = href.split('/')[-1]
            # print(file_name)
            # print(file_name.split('.'))
            if file_name.split('.')[-1] == 'ppt':
                save_pdf(href)
        except:
            continue


def save_pdf(href):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url+href, headers=kv)
        print(url+href)
        path = root + href.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份pdf")
    except:
        return ""


if __name__ == '__main__':
    start_url = 'http://www.andrew.cmu.edu/course/95-707/'
    url = 'http://www.andrew.cmu.edu/course/95-707/lecture/'
    root = './/download-single//'
    if not os.path.exists(root):
        os.mkdir('.//download-single')
    get_ref(start_url)
