from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# Test Case 1: Forgot Password Link Validation on Login Page (TC_PIM_01) - Positive
def test_forgot_password():
    driver.get(url)
    try:
        # Wait for the "Forgot your password?" link to be visible and then click it
        forgot_password_link = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'orangehrm-login-forgot-header')]"))
        )
        forgot_password_link.click()

        # Ensure the Username textbox is visible
        username_box = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )

        username_box.send_keys("Admin")  # Provide username

        # Click on "Reset Password"
        reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        reset_button.click()

        # Validate the successful reset message
        success_message = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Reset Password link sent successfully')]"))
        )

        print("TC_PIM_01: Passed")

    except NoSuchElementException as e:
        print(f"TC_PIM_01: Failed - {e}")
    except TimeoutException as e:
        print(f"TC_PIM_01: Failed - {e}")

# Test Case 1: Forgot Password Link Validation on Login Page (TC_PIM_01) - Negative
# Scenario: Attempting to reset the password with a non-existent username
def test_forgot_password_negative():
    driver.get(url)
    try:
        # Wait for the "Forgot your password?" link to be visible and then click it
        forgot_password_link = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'orangehrm-login-forgot-header')]"))
        )
        forgot_password_link.click()

        # Ensure the Username textbox is visible
        username_box = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )

        username_box.send_keys("nonexistentuser")  # Provide a non-existent username

        # Click on "Reset Password"
        reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        reset_button.click()

        # Validate the error message
        error_message = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'No account found with that username')]"))
        )

        print("TC_PIM_01 (Negative): Passed")

    except NoSuchElementException as e:
        print(f"TC_PIM_01 (Negative): Failed - {e}")
    except TimeoutException as e:
        print(f"TC_PIM_01 (Negative): Failed - {e}")


if __name__ == "__main__":
    # Positive test cases
    print("Running Positive Test Case:")
    test_forgot_password()

    # Clear cookies or reset the session to ensure a clean state for the next test
    driver.delete_all_cookies()
    driver.get(url)

    # Negative test cases
    print("Running Negative Test Case:")
    test_forgot_password_negative()

    driver.quit()
