from selenium import webdriver
from selenium.webdriver.common.by import By

high  = driver.find_element(By.XPATH, "//input[contains(@id, 'user_name')]")

high = driver.find_element(By.XPATH, "//li[position()=3]")

high = driver.find_element(By.XPATH, "//input[contains(text()='high')]")