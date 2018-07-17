import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from time import sleep


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.228.com.cn/venuesearch/1/?cityid=sh")

