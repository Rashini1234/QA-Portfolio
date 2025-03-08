from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open SauceDemo website
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify login success
    if "inventory" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")
        driver.quit()
        exit()

    # Add an item to the cart
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()

    # Verify the cart count
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    cart_count = cart_badge.text

    if cart_count == "1":
        print("Add to Cart Test Passed!")
    else:
        print("Add to Cart Test Failed!")

except Exception as e:
    print(f"Test failed due to error: {e}")

finally:
    # Close the browser
    time.sleep(3)
    driver.quit()
