import requests
from bs4 import BeautifulSoup
import os


def get_ref(start_url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(start_url, headers=kv, proxies=proxies)
        r.raise_for_status()
    except:
        print("failed to get the start url")
        return

    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)
        try:
            file_name = href.split('/')[-1]
            # print(file_name)
            # print(file_name.split('.'))
            if file_name.split('.')[-1] == 'pdf':
                save_pdf(href)
        except:
            continue


def save_pdf(href):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        print(href)
        r = requests.get(href, headers=kv, proxies=proxies)
        path = root + href.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份pdf")
    except:
        return ""


if __name__ == '__main__':
    start_url = 'http://cs231n.stanford.edu/syllabus.html'
    # url = 'http://cs231n.stanford.edu/slides/2017/'
    root = './/download-single//'
    if not os.path.exists(root):
        os.mkdir('.//download-single')

    """
    can refer:
    http://docs.python-requests.org/en/latest/user/advanced/#proxies
    
    proxies = {
        "http": "10.10.1.10:3128",
        "https": "10.10.1.10:1080",    
    }
    """
    proxies = {
        "http": "http://user:pass@10.10.1.10:8888/"
    }
    get_ref(start_url)
