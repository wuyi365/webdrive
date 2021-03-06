# coding = utf-8

from selenium import webdriver

import os, time

weburl = 'http://sf1-wbroci102.analytics.moodys.net/ro/login.html'
timesleep = 5

chromedriver = "C:\dev\chromedriver_win32\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

print('initing broswer begins..')
browser = webdriver.Chrome(chromedriver)
time.sleep(2)
print('initing broswer done..')

# open browser to the url
#
browser.get(weburl)
time.sleep(1)
print(chromedriver.title)
print('begin to send key')

# enter username and password
#
browser.find_element_by_name("username").send_keys('admin')
browser.find_element_by_name("password").send_keys('admin')
time.sleep(0.5)
print('begin to click login button')
#browser.find_element_by_class_name("btn btn-primary btn-sm").click()
browser.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
print('click login button done')

# wait a while to load home page
#
time.sleep(10)

browser.find_element_by_xpath("//*[contains(text(), 'Entity Management')]").click()
time.sleep(5)
browser.find_element_by_xpath("//*[contains(text(), 'Entity Search')]").click()
#browser.find_element_by_link_text('Entity Search').click()
time.sleep(0.5)

browser.find_element_by_id('LongName').send_keys('test')
browser.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()

time.sleep(5)
browser.quit()