from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:
    LOGIN_FIELD = 'user-name'
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = 'input[type="submit"]'


class Creds:
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'


driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"
driver.get(url)
login_field = driver.find_element(By.ID, Locators.LOGIN_FIELD)
password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
login_btn = driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON)
login_field.send_keys(Creds.USERNAME)
password_field.send_keys(Creds.PASSWORD)
login_btn.click()
expected_url = "https://www.saucedemo.com/inventory.html"

assert driver.current_url == expected_url

driver.close()


