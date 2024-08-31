from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# Test Case 3: Main Menu Validation on Admin Page (TC_PIM_03) - Positive
def test_main_menu_validation_admin():
    driver.get(url)
    try:
        # Log in as Admin
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()

        # Navigate to Admin page
        admin_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/admin')]"))
        )
        admin_tab.click()

        # Validate the main menu options on Admin page
        expected_menu_items = [
            "Admin", "PIM", "Leave", "Time", "Recruitment", "My Info",
            "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"
        ]

        for item in expected_menu_items:
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//span[text()='{item}']"))
            ), f"Menu item {item} is not visible"

        print("TC_PIM_03: Passed")

    except NoSuchElementException as e:
        print(f"TC_PIM_03: Failed - {e}")
    except TimeoutException as e:
        print(f"TC_PIM_03: Failed - {e}")

# Test Case 3: Main Menu Validation on Admin Page (TC_PIM_03) - Negative
# Scenario: Verifying that an unauthorized user cannot see the Admin menu options
def test_main_menu_validation_admin_negative():
    driver.get(url)
    try:
        # Log in as a non-admin user (assuming you have credentials for such a user)
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("NonAdminUser")
        password.send_keys("nonadminpassword")
        login_button.click()

        # Attempt to access Admin page
        admin_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/admin')]"))
        )

        if admin_tab:
            print("TC_PIM_03 (Negative): Failed - Admin tab should not be visible for non-admin users.")
        else:
            print("TC_PIM_03 (Negative): Passed - Admin tab is not visible for non-admin users.")

    except NoSuchElementException:
        print("TC_PIM_03 (Negative): Passed - Admin tab is not visible for non-admin users.")
    except TimeoutException as e:
        print(f"TC_PIM_03 (Negative): Failed - {e}")

if __name__ == "__main__":
    # Positive test cases
    test_main_menu_validation_admin()

    # Negative test cases
    test_main_menu_validation_admin_negative()

    driver.quit()
