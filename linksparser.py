# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print("Login mos.ru:")
my_login = input()
print("Password mos.ru:")
my_password = input()
print("Number of weeks:")
counter = int (input())

url_avt = 'https://www.mos.ru/pgu/ru/application/dogm/journal/'
current_url = ''
xpath_mos_login = '/html/body/div[1]/section/section/div[2]/form/div[1]/div/div/input'
xpath_mos_password = '/html/body/div[1]/section/section/div[2]/form/div[2]/div/input'
xpath_7days = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div/div'
xpath_lesson_name = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div'
xpath_lesson_time = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div'
xpath_lesson_back = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/div/div[1]/div'
xpath_next_week = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[3]'
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
j = 0
null = []

#key_enter = u'\ue007'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get (url_avt)
driver.find_element_by_xpath(xpath_mos_login).send_keys(my_login)
driver.find_element_by_xpath(xpath_mos_password).send_keys(my_password, u'\ue007')
time.sleep(20)
driver.find_element_by_xpath(xpath_7days).click()
time.sleep(10)
file = open('links.txt', 'w')

for i in range (counter):
    xpath_day = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div[1]'
    for i in range(2, 7):
        print (days[j])
        file.write(days[j] + '\n')
        j +=1
        while driver.find_elements_by_xpath(xpath_day) != null:
            driver.find_element_by_xpath(xpath_day).click()
            time.sleep(3)
            print (driver.find_element_by_xpath(xpath_lesson_time).get_attribute("textContent"))
            file.write(driver.find_element_by_xpath(xpath_lesson_time).get_attribute("textContent") + '\n')
            print (driver.find_element_by_xpath(xpath_lesson_name).get_attribute("textContent"))    
            file.write(driver.find_element_by_xpath(xpath_lesson_name).get_attribute("textContent") + '\n')
            lesson_id = driver.current_url[-16:-7]
            conference_link = 'https://dnevnik.mos.ru/conference/?scheduled_lesson_id=' + lesson_id
            print (conference_link)
            file.write(conference_link + '\n' + '\n')
            print()
            driver.find_element_by_xpath(xpath_lesson_back).click()
            time.sleep(4)
            xpath_day = xpath_day[:-2] + str(int(xpath_day[-2]) + 2) + ']'
       #xpath_day = xpath_day[:85] + str(i) + xpath_day[86:-2] + '1' + ']'
        xpath_day = '//*[@id="root"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div/div[' + str(i) + ']/div[2]/div/div[1]'
        time.sleep(1)
    driver.find_element_by_xpath (xpath_next_week).click()
    j = 0
file.close()
print ("Links saved in links.txt")
