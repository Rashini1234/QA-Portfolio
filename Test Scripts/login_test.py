from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Maximize window
driver.maximize_window()

# Perform Login
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Verify successful login
if "inventory" in driver.current_url:
    print("Login Test Passed!")
else:
    print("Login Test Failed!")

# Close the browser
time.sleep(3)
driver.quit()
