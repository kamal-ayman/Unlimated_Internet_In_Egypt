import ctypes
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def Bot(user, password, hashtag):
    driver = webdriver.Chrome()
    driver.get('https://twitter.com/login/')
    sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@autocomplete='username']").send_keys(user + Keys.ENTER)
    sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@autocomplete='current-password']").send_keys(password + Keys.ENTER)
    sleep(1)
    driver.get('https://twitter.com/search?q=%23انترنت_غير_محدود_في_مصر&src=trend_click&f=live&vertical=trends')
    sleep(3)
    i = 0
    ran = str(random.randint(1, 9999))

    while 1:
        try:
            print(i)
            driver.find_element(by=By.XPATH, value="//a[@data-testid='SideNav_NewTweet_Button']").click()
            sleep(.5)
            driver.find_element(by=By.XPATH, value="//div[@role='textbox']").send_keys(
                hashtag+' \n '+str(i)+ran
                # Keys.CONTROL + 'v'
            )
            sleep(.2)
            driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()
            i += 1
            sleep(.5)
        except:
            ran = str(random.randrange(1, 9999))
            continue


def main():
    try:
        hashtag = open('hashtag.txt', 'r', encoding='utf-8').read()
    except:
        hashtag = open('hashtag.txt', 'w+')
        ctypes.windll.user32.MessageBoxW(0, 'new file \'hashtag.txt\' created please add your text...', "Warning")
        return
    if hashtag == '':
        ctypes.windll.user32.MessageBoxW(0, "please Enter something in hashtag file!", "Warning")
        return

    try:
        acc = open('account.txt', 'r').read()
        user = acc.split(':')[0]
        password = acc.split(':')[1]
    except:
        user = input('Enter user name: ')
        password = input('Enter password: ')
        open('account.txt', 'w+').write(user + ':' + password)

    print('username: ' + user)
    print('password: ' + password)
    print('login now ...')

    try:
        Bot(user, password, hashtag)
    except:
        ctypes.windll.user32.MessageBoxW(0, "please install Google Chrome", "Error")


if __name__ == '__main__':
    if os.path.isfile('chromedriver.exe'):
        main()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Where is the googledriver.exe?\ni can\'t see it ! ", "Error")
