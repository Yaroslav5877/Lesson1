# from selenium import webdriver
# from time import sleep

# chrome = webdriver.Chrome()
# firefox = webdriver.Firefox()
# # //button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]
# try:
    
#     chrome.get("http://uitestingplayground.com/classattr")
#     firefox.get("http://uitestingplayground.com/classattr")
    
#     for _ in range(3):
#         blue_button_chrome = chrome.find_element(
#             "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
#         blue_button_chrome.click()
        
#         blue_button_firefox = firefox.find_element(
#             "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
#         blue_button_firefox.click()
        
#         sleep(2)
        
#         chrome.switch_to.alert.accept()
#         firefox.switch_to.alert.accept()
        
# except Exception as ex:
#     print(ex)
# finally:
#     chrome.quit()
#     firefox.quit()


# Немного доработанный скрипт
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    # Открытие страницы в обоих браузерах
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")
    
    for _ in range(3):
        # Поиск и клик по кнопке в Chrome
        blue_button_chrome = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button_chrome.click()
        
        # Поиск и клик по кнопке в Firefox
        blue_button_firefox = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button_firefox.click()
        
        sleep(2)
        
        # Закрытие всплывающих окон, если они появляются
        try:
            chrome.switch_to.alert.accept()
        except:
            pass
        
        try:
            firefox.switch_to.alert.accept()
        except:
            pass
        
except Exception as ex:
    print(f"Произошла ошибка: {ex}")
    
finally:
    chrome.quit()
    firefox.quit()
