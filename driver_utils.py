from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to initialize the web driver and open the website
def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("http://sdetchallenge.fetch.com/")
    return driver

# Function to click the Weigh button
def click_weigh(driver):
    driver.find_element(By.ID, "weigh").click()

# Function to click the Reset button
def click_reset(driver):
    driver.find_elements(By.ID, "reset")[1].click() # Referencing second element with id="reset" as there are 2 elements with same ID

# Function to input gold bar numbers in the bowls
def fill_bowls(driver, left_bowl, right_bowl):
    for i in range(len(left_bowl)):
        left_grid = driver.find_element(By.ID, f"left_{i}")
        right_grid = driver.find_element(By.ID, f"right_{i}")

        left_grid.send_keys(left_bowl[i])
        right_grid.send_keys(right_bowl[i])
