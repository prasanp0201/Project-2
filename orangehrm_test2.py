from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# Test Case: TC_Login_01 - Successful Employee login to OrangeHRM portal
def test_login_successful():
    driver.get(url)
    
    # Use WebDriverWait to wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    
    # Enter username and password
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    
    # Click on the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Check if login was successful
    try:
        # Use WebDriverWait to wait for the welcome message to be visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.oxd-userdropdown-name")))
        welcome_text = driver.find_element(By.CSS_SELECTOR, "p.oxd-userdropdown-name").text
        assert "Paul Collings" in welcome_text
        print("Test Case TC_Login_01 Passed: User logged in successfully.")
    except NoSuchElementException:
        print("Test Case TC_Login_01 Failed: Login unsuccessful.")
    
    time.sleep(2)  # Optional sleep for visual confirmation

# Test Case: TC_Login_02 - Invalid Employee login to OrangeHRM portal
def test_login_invalid_password():
    driver.get(url)
    
    # Use WebDriverWait to wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    
    # Enter username and incorrect password
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("InvalidPassword")
    
    # Click on the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Check for error message
    try:
        # Use WebDriverWait to wait for the error message to be visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.oxd-alert-content-text")))
        error_message = driver.find_element(By.CSS_SELECTOR, "p.oxd-alert-content-text").text
        assert "Invalid credentials" in error_message
        print("Test Case TC_Login_02 Passed: Correct error message displayed.")
    except NoSuchElementException:
        print("Test Case TC_Login_02 Failed: Error message not displayed.")
    
    time.sleep(2)

# Test Case: TC_PIM_01 - Add a new employee in the PIM module
def test_add_employee():
    # Assuming the user is already logged in
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()
    
    # Fill in employee details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("John")
    driver.find_element(By.NAME, "lastName").send_keys("Doe")
    
    # Save the employee
    driver.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary").click()
    
    # Verify that employee is added
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-toast-container"))
        ).text
        assert "Success" in success_message
        print("Test Case TC_PIM_01 Passed: Employee added successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_01 Failed: Employee not added.")
    
    time.sleep(2)

# Test Case: TC_PIM_02 - Edit an existing employee in the PIM module
def test_edit_employee():
    # Assuming the user is already logged in
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()
    
    # Click on an employee name to edit (assuming first employee in the list)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='John Doe']"))).click()
    
    # Edit employee details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--secondary"))).click()
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    first_name_field.clear()
    first_name_field.send_keys("Johnny")
    driver.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary").click()
    
    # Verify that employee is edited
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-toast-container"))
        ).text
        assert "Success" in success_message
        print("Test Case TC_PIM_02 Passed: Employee edited successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_02 Failed: Employee not edited.")
    
    time.sleep(2)

# Test Case: TC_PIM_03 - Delete an existing employee in the PIM module
def test_delete_employee():
    # Assuming the user is already logged in
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()
    
    # Select the checkbox for an employee (assuming first employee in the list)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"))
    ).click()
    
    # Click delete
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--label-danger"))).click()
    
    # Confirm deletion
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--label-danger"))).click()
    
    # Verify that employee is deleted
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-toast-container"))
        ).text
        assert "Success" in success_message
        print("Test Case TC_PIM_03 Passed: Employee deleted successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_03 Failed: Employee not deleted.")
    
    time.sleep(2)

# Run all tests
test_login_successful()
test_login_invalid_password()
test_add_employee()
test_edit_employee()
test_delete_employee()

# Close the browser window
driver.quit()
