from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://twitter.com/login/')

i = 0
input("Login first and press enter!!")
driver.get('https://twitter.com/search?q=%23انترنت_غير_محدود_في_مصر&src=trend_click&f=live&vertical=trends')

sleep(7)
while 1:
    driver.find_element(by=By.XPATH, value="//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(.1)
    driver.find_element(by=By.XPATH, value="//div[@role='textbox']").send_keys(f"_{i} #انترنت_غير_محدود_في_مصر {i}\n #Unlimated_Internet_In_Egypt {i}")
    driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()
    i += 1
    sleep(.5)
