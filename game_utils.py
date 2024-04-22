from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to get the measurement result
def get_measurement(driver):
    time.sleep(3)  # Add a delay to allow the measurement result to appear
    game_info = driver.find_element(By.CLASS_NAME, "game-info")
    weighings = game_info.find_element(By.TAG_NAME, "ol").find_elements(By.TAG_NAME, "li")
    weighing_results = [weighing.text for weighing in weighings]
    operator = driver.find_element(By.CLASS_NAME, "result").find_element(By.ID, "reset").text
    return weighing_results, operator

# Function to click the fake gold bar number and check the alert message
def check_fake_bar(driver, fake_bar_number):
    fake_bar_button = driver.find_element(By.ID, f"coin_{fake_bar_number}")
    fake_bar_button.click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_message = alert.text
    alert.accept()
    return alert_message
