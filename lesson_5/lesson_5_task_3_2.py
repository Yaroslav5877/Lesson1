from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count = 0
    
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")
    
    for _ in range(3):
        blue_button_chrome = chrome.find_element(
            "xpath", '//button [text()="Button with Dynamic ID"]')
        blue_button_chrome.click()
        
        blue_button_firefox = firefox.find_element(
            "xpath", '//button [text()="Button with Dynamic ID"]')
        blue_button_firefox.click()
        
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
    print(f'Произошла ошибка: {ex}')
finally:
    chrome.quit()
    firefox.quit()
        
        
        