# -*- coding: utf-8 -*-  

from selenium import webdriver

import os, time

import codecs

weburl = 'http://www.66rpg.com/'
weburl = 'http://passport.66rpg.com/user/cross.shtml?fromurl=http%3A%2F%2Fwww.66rpg.com%2Findex&auth_callback=http%3A%2F%2Fwww.66rpg.com%2Fsso%2Fauth_callback&app=www&sign=ac96024fe2415fbf76f8f6f3bdabb365&login_type=0'
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
# click login
#
#browser.find_element_by_xpath("//span[@class='un_login'][1]").click()
#browser.find_element_by_xpath("//div[@class='user-box fr']").click()

#browser.find_element_by_partial_link_text(u'登录').click()
time.sleep(3)
# enter username and password
#

with codecs.open('u.txt', "r",encoding='utf-8', errors='ignore') as fdata:
	strs = fdata.read()
#strs = u"放开那个猕猴桃"

print(type(strs))


browser.find_element_by_id("username").send_keys(strs)
browser.find_element_by_name("password").send_keys('110119rick')
time.sleep(0.5)
print('begin to click login button')
#browser.find_element_by_class_name("btn btn-primary btn-sm").click()
#browser.find_element_by_xpath("//button[@class='login_btn fl']").click()
browser.find_element_by_xpath("//div[@class='login_btn_box']").click()


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