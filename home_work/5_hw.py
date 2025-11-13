from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    text_field_username = driver.find_element(By.CSS_SELECTOR, '[id="user-name"]')
    text_field_password = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
    button_submit = driver.find_element(By.CSS_SELECTOR, '[id="login-button"]')
    if text_field_username and text_field_password and button_submit:
        print('Элементы найдены')