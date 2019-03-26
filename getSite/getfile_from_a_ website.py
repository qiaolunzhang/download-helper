import requests
from bs4 import BeautifulSoup
import os


def getLoc(start_url):
    try:
        #start_url = 'http://ipads.se.sjtu.edu.cn/courses/ics/schedule.shtml'
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(start_url, headers=kv)
        r.raise_for_status()
    except:
        print("爬取失败")
        return ""
    demo = r.text
    print(demo)
    soup = BeautifulSoup(demo, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
    for link in soup.find_all('a'):
        loc = link.get('href')
        try:
            flag = loc.find('pdf')
            if (flag >= 0):
                savePdf(loc)
                continue
        except:
            continue
        try:
            flag = loc.find('ppt')
            if (flag >= 0):
                savePpt(loc)
                continue
        except:
            continue
        try:
            flag = loc.find('txt')
            if (flag >= 0):
                saveTxt(loc)
                continue
        except:
            continue
    print("完成")



    return 0

def savePdf(loc):
    #url = 'http://ipads.se.sjtu.edu.cn/courses/ics/'
    #root = './/download//'
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url+loc, headers=kv)
        path = root + 'pdf//' + loc.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("一份pdf")
    except:
        return ""

def savePpt(loc):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url+loc, headers=kv)
        path = root + 'ppt_pptx//' + loc.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("一份ppt")
    except:
        return ""

def saveTxt(loc):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url+loc, headers=kv)
        path = root + 'txt//' + loc.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份txt")
    except:
        return ""

if __name__ == '__main__':
    start_url = "http://cs.brown.edu/courses/csci0150/lectures.html"
    url = "http://cs.brown.edu/courses/csci0150/docs/lectures/"
    if not os.path.exists('.//download'):
        os.mkdir('.//download')
    root = './/download//'
    if not os.path.exists(root+'pdf'):
        os.mkdir(root+'pdf')
    if not os.path.exists(root+'ppt_pptx'):
        os.mkdir(root+'ppt_pptx')
    if not os.path.exists(root+'txt'):
        os.mkdir(root+'txt')
    getLoc(start_url)
