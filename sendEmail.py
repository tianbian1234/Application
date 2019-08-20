from selenium import webdriver
import sys, time

dr = webdriver.Firefox(executable_path = '/Users/a/Downloads/geckodriver')

dr.get('https://www.mail.qq.com/')

dr.switch_to_frame('login_frame')

time.sleep(2)

switcherElem = dr.find_element_by_id('switcher_plogin')
switcherElem.click()

emailElem = dr.find_element_by_id('u')
emailElem.send_keys('2232683849')
passwordElem = dr.find_element_by_id('p')
passwordElem.send_keys('15030595009')
submitElem = dr.find_element_by_id('login_button')
submitElem.click()

time.sleep(5)

dr.switch_to_default_content()

dr.find_element_by_id('composebtn').click()

dr.switch_to_frame('mainFrame')
time.sleep(2)

dr.find_element_by_id('toAreaCtrl').send_keys(sys.argv[1])
dr.find_element_by_id('subject').send_keys(sys.argv[2])

time.sleep(2)

dr.find_element_by_class_name('sendbtn').click()

