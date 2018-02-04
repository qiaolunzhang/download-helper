import requests
from bs4 import BeautifulSoup
import os


def get_ref(start_url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(start_url, headers=kv)
        r.raise_for_status()
    except:
        print("failed to get the start url")
        return

    text = r.text
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
            if file_name.split('.')[-1] == 'pdf':
                save_pdf(href)
        except:
            continue


def save_pdf(href):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url+href, headers=kv)
        path = root + href.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份pdf")
    except:
        return ""


if __name__ == '__main__':
    start_url = 'http://www.cs.cornell.edu/courses/cs1133/2017fa/lectures/index.php'
    url = 'http://www.cs.cornell.edu/courses/cs1133/2017fa/lectures/'
    root = './/download-single//'
    if not os.path.exists(root):
        os.mkdir('.//download-single')
    get_ref(start_url)
