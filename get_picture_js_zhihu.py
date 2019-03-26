import requests
import re
from bs4 import BeautifulSoup
import os


def parse_page(start_url, err_url):
    for one_url in start_url:
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
            r = requests.get(one_url, headers=header)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            text = r.text
            # soup = BeautifulSoup(text, parser='html-parser')
        except:
            print("failed to download", one_url)

        imgs = []
        jpg = re.compile(r'https://[^\s]*?.jpg')
        jpeg = re.compile(r'https://[^\s]*?.jpeg')
        gif = re.compile(r'https://[^\s]*?.gif')
        png = re.compile(r'https://[^\s]*?.png')

        imgs += jpg.findall(text)
        imgs += jpeg.findall(text)
        imgs += gif.findall(text)
        imgs += png.findall(text)

        for img in imgs:
            folder = one_url.split('/')[-1]
            try:
                download(img, folder)
            except:
                err_url.append(img)


def download(img, folder):
    root = './/' + folder
    if not os.path.exists(root):
        os.mkdir(root)
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    try:
        r = requests.get(img, headers=header)
        path = root + '//' + img.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('一张图片')
    except:
        err_url.append(img)

    print(img)


if __name__ == '__main__':
    start_url = ['https://www.zhihu.com/question/22212644']
    err_url = []
    parse_page(start_url, err_url)
