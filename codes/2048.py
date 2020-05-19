#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://play2048.co/')

html = browser.find_element_by_tag_name('html')

score = ['0','0']

while True:

    #browser.get('https://play2048.co/')

    #html = browser.find_element_by_tag_name('html')
    
    spam = 1
    
    while spam != 0:
        try:
            browser.find_element_by_css_selector('body > div.container > \
div.game-container > div.game-message.game-over > div > a.retry-button') == '0$'
            spam = 0
        except:
            html.send_keys(Keys.LEFT)
            html.send_keys(Keys.UP)
            html.send_keys(Keys.RIGHT)
            html.send_keys(Keys.DOWN)
            

    scr = browser.find_element_by_css_selector('body > div.container > \
div.heading > div > div.score-container').text
    
    score = scr.split('\n')
    
    print('The score is ' + score[0] + '.')

    time.sleep(4)
    
    if int(score[0]) < 10000:

        print('Something')
        browser.find_element_by_link_text('Try again').click()
        
    else:
        break
