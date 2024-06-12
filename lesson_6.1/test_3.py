from data import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"

first_name = "Иван"
last_name = "Иванов"
postal_code = "123456"


expected_total = "$58.29"

def test_purchase():
    browser = webdriver.Chrome()

    try:
        
        browser.get(URL_3)

        
        browser.find_element(By.ID, "user-name").send_keys(username)
        browser.find_element(By.ID, "password").send_keys(password)
        browser.find_element(By.ID, "login-button").click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        browser.find_element(By.ID, "first-name").send_keys(first_name)
        browser.find_element(By.ID, "last-name").send_keys(last_name)
        browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        browser.find_element(By.ID, "continue").click()

        total_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text

        assert total_text == f"Total: {expected_total}", f"Expected total to be '{expected_total}', but got '{total_text}'"
        print(f"Итоговая сумма равна ${expected_total}")
    
    finally:
        
        browser.quit()

if __name__ == "__main__":
    test_purchase()
