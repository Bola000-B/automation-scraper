from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import os
import csv
import time


driver = webdriver.Chrome()

class Parts():
    def __init__(self):
        pass

    def processor(self,name):
        driver.get("https://www.techpowerup.com/cpu-specs/")
        b_search = driver.find_element(By.CSS_SELECTOR,"input.js-search-input").send_keys(name)

        time.sleep(5)

    def g_card(self):
        pass

    def m_board(self):
        pass

object = Parts()

part_type = input("enter part type (cpu, gpu, mother board): or exit to exit:  ").lower().strip()

while True:
    reorder = input("you want to continue?  write (y or n): ").lower().strip()

    if reorder == "y":
        pass

    elif reorder =="n" :
        break
    
    else:
        print("please recheck your character and try again")


    if part_type == "cpu":
        part_name = input("write processor name: ")
        object.processor(part_name)

    elif part_type == "gpu":
        part_name = input("write graphic card name :")
        object.g_card()

    elif part_type == "mother board":
        part_name = input("write mother board name: ")
        object.m_board()

    elif part_type == "exit":
        break
    
    else:
        print("please recheck your character and try again")