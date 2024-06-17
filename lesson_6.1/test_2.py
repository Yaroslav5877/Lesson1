from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *

def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)
    
    delay_input = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys(45)
    
    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '7']"))
    ).click()
    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '+']"))
    ).click()
    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '8']"))
    ).click()
    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '=']"))
    ).click()
    
    result = WebDriverWait(chrome_browser, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text
    
    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'"

    input("Press Enter to close the browser...")

if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    try:
        test_calculator_form(browser)
    finally:
        browser.quit()
