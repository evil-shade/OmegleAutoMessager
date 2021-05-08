from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

message = "Hello there "


def run():
    driver.get('https://www.omegle.com/')
    time.sleep(2)
    element = driver.find_element_by_id('textbtn')
    element.click()
    time.sleep(1)
    element = driver.find_element_by_class_name('chatmsg')
    time.sleep(1.5)
    element.send_keys('hi')
    element.send_keys(Keys.RETURN)
    time.sleep(2)
    # while loop ah pottu chat msg dissable ika nu check pannu
    if driver.find_element_by_class_name('chatmsg'):
        for i in message:
            element.send_keys(i)
            time.sleep(0.1)
        element.send_keys(Keys.RETURN)


if __name__ == '__main__':
    run()
