import requests
import os

def save_pdf(href):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        print(url+href)
        r = requests.get(url+href, headers=kv)
        path = root + href.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份pdf")
    except:
        return ""
'''
def save_pdf(href):
    kv = {'user-agent': 'Mozilla/5.0'}
    print(url+href)
    r = requests.get(url+href, headers=kv)
    path = root + href.split('/')[-1]
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
    print("一份pdf")
'''

if __name__ == '__main__':
    url = 'http://staff.ustc.edu.cn/~billzeng/ns/'
    root = './/download-single//'
    if not os.path.exists(root):
        os.mkdir('.//download-single')
    for i in range(1, 15):
        if i < 10:
            save_pdf('ns'+'0'+str(i)+'.pdf')
        else:
            save_pdf('ns'+str(i)+'.pdf')
