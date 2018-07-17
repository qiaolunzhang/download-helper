import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from time import sleep

def getSiteInfo(url):
    try:
        url = "https:" + url
        driver = webdriver.Firefox()
        driver.get(url)
        r = driver.page_source
        #driver.quit()
        driver.close()
        soup = BeautifulSoup(r, "html.parser")
        info = soup.find('p', attrs={"class": "venue-detail-content clearfloat"})
        return info.string
    except:
        return ""

def getOnePage(url):
    driver = webdriver.Firefox()
    driver.get(url)
    r = driver.page_source
    # driver.quit()
    driver.close()
    soup = BeautifulSoup(r, 'html.parser')

    for link in soup.find_all('dl', attrs={"class": "venue-cont-listdl"}):
        info = ""
        name = link.find_all("img")
        #print(name)
        name = name[0].get("alt")
        name = name.strip()
        print(name)
        info = info + name + " , "

        site = link.find_all('p', attrs={"class": "venue-cont-listdlb"})
        site = site[0].string
        site = site.strip()
        print(site)
        info = info + site + " , "

        site_link = link.find_all('a')
        site_link = site_link[0].get("href")
        site_link = getSiteInfo(site_link)
        site_link = site_link.strip()
        print(site_link)
        info = info + site_link + '\n'

        try:
            with open("./site1.csv", "a+") as f:
                f.write(info)
        except:
            continue


if __name__ == '__main__':
    baseurl = "https://www.228.com.cn/venuesearch/"
    for i in range(16, 39):
        url = baseurl + str(i) + "/?cityid=sh"
        getOnePage(url)


