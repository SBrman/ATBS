#! python3

import os
from selenium import webdriver

os.chdir('C:\\Users\\Simanta\\AppData\\Local\\Programs\\Python\\Python38')
browser = webdriver.Chrome()

browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name.')
