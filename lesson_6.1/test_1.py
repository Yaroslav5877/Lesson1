from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *
from time import sleep

def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    form_data = {
        "first-name": first_name,
        "last-name": last_name,
        "address": address,
        "e-mail": email,
        "phone": phone_number,
        "zip-code": zip_code,
        "city": city,
        "country": country,
        "job-position": job_position,
        "company": company
    }
    
    for field_name, value in form_data.items():
        print(f"Заполняем поле: {field_name} значением {value}")
        field = WebDriverWait(chrome_browser, 10).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.send_keys(value)
        
    submit_button = WebDriverWait(chrome_browser, 40).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    submit_button.click()
    sleep(10)
    
    field_classes = {
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "zip-code": "danger",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success"
    }
    
    for field_id, class_name in field_classes.items():
        print(f"Проверяем поле: {field_id} на наличие класса: {class_name}")
        field = WebDriverWait(chrome_browser, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        field_class = field.get_attribute("class")
        print(f"Класс элемента: {field_class}")
        assert class_name in field_class, f"Поле {field_id} должно содержать класс {class_name}"

if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    try:
        test_data_types_form(browser)
    finally:
        browser.quit()
