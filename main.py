from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


        # get link and open new tab
        time.sleep(1)
        print("please wait")
        time.sleep(4)
        try:
            item= driver.find_element(By.CSS_SELECTOR, "div.items-mobile--item a.item-name").get_attribute('href')
        except:
            print("error in h-ref item")

        driver.switch_to.new_window("tab")
        driver.get(item)

        # get item specifications
        generation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[text()='Generation:']/following-sibling::td"))).text.split("\n")[1]
        core = driver.find_element(By.XPATH, "//th[text()='# of Cores:']/following-sibling::td").text
        thread = driver.find_element(By.XPATH, "//th[text()='# of Threads:']/following-sibling::td").text
        frequency = driver.find_element(By.XPATH, "//th[text()='Frequency:']/following-sibling::td").text
        turbo_clock = driver.find_element(By.XPATH, "//th[text()='Turbo Clock:']/following-sibling::td").text
        socket = driver.find_element(By.XPATH, "//th[text()='Socket:']/following-sibling::td/a").text
        process_size = driver.find_element(By.XPATH, "//th[contains(text(),'Process Size:')]/following-sibling::td").text
        l3_cache = driver.find_element(By.XPATH, "//th[text()='Cache L3:']/following-sibling::td").text
        try:
            launch_price = driver.find_element(By.XPATH, "//th[text()='Launch Price:']/following-sibling::td").text
        except:
            launch_price = None
        memory_support = driver.find_element(By.XPATH, "//th[text()='Memory Support:']/following-sibling::td").text
        pci_express = driver.find_element(By.XPATH, "//th[text()='PCI-Express:']/following-sibling::td").text
        tdp = driver.find_element(By.XPATH, "//th[text()='TDP:']/following-sibling::td").text


        time.sleep(5)



    def g_card(self):
        pass

    def m_board(self):
        pass

object = Parts()


while True:
    reorder = input("you want to continue?  write (y or n): ").lower().strip()

    if reorder == "y":
        part_type = input("enter part type (cpu, gpu, mother board): or exit to exit:  ").lower().strip()

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

    elif reorder =="n" :
        break
    
    else:
        print("please recheck your character and try again")



if driver:
    driver.quit()