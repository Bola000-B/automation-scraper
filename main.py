from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as UC
import time
import os
import folders



UC.Chrome.__del__ = lambda self: None
if __name__ == "__main__":
    driver = UC.Chrome(use_subprocess=False, version_main=150)


    class Parts():
        def __init__(self):
            self.path()

        def path(self):
            if os.path.exists("path.txt"):
                path = input("you want to change the path (y or n)").lower()
                if path == "y":
                    self.new_path = input("what is new path: ")
                    with open("path.txt", "w") as file:
                        file.write(self.new_path)

                else:
                    with open("path.txt", "r") as file:
                        self.new_path = file.read().strip()

            else:
                self.new_path = input("please type a path: ")
                with open("path.txt", "w") as file:
                    file.write(self.new_path)



        def processor(self,name):
            driver.get("https://www.techpowerup.com/cpu-specs/")
            b_search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.js-search-input"))).send_keys(name)


            # get link and open new tab
            time.sleep(4)
            try:
                item= driver.find_element(By.CSS_SELECTOR, "div.items-mobile--item a.item-name").get_attribute('href')
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


                file_c = os.path.join(self.new_path, f"cpu_{name}.txt")
                with open(rf"{file_c}","w") as file:
                    file.write(f"               {name.upper()}              \n")
                    file.write(f"Generation: {generation}\n")
                    file.write(f"Core: {core}\n")
                    file.write(f"Thread: {thread}\n")
                    file.write(f"Frequency: {frequency}\n")
                    file.write(f"Turbo_clock: {turbo_clock}\n")
                    file.write(f"Socket: {socket}\n")
                    file.write(f"Process_Size: {process_size}\n")
                    file.write(f"L3_cach: {l3_cache}\n")
                    file.write(f"Launch_Price: {launch_price}\n")
                    file.write(f"Memory_Support: {memory_support}\n")
                    file.write(f"Pci_express{pci_express}\n")
                    file.write(f"TDP: {tdp}\n")

                driver.close()
                driver.switch_to.window(driver.window_handles[0])



            except:
                print("error in h-ref item")




        def g_card(self, name):
            driver.get("https://www.techpowerup.com/gpu-specs/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='js-search-input search-input']"))).send_keys(name)
            
            time.sleep(2)
            try:
                item = driver.find_element(By.CSS_SELECTOR, "a.item-name").get_attribute("href")
                driver.switch_to.new_window("tab")
                driver.get(item)

                time.sleep(3)

                # All_name - اسم الكرت كامل
                all_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.gpudb-name"))).text

                # Architecture - المعمارية
                architecture = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//dt[text()='Architecture']/following-sibling::dd"))).text
                
                # Process Size - دقة التصنيع
                processor_size = driver.find_element(By.XPATH, "//dt[text()='Process Size']/following-sibling::dd").text
                
                # Memory Size (VRAM) - حجم الذاكرة
                memory_size = driver.find_element(By.XPATH, "//dt[text()='Memory Size']/following-sibling::dd").text

                # Memory Type - نوع الذاكرة
                memory_type = driver.find_element(By.XPATH, "//dt[text()='Memory Type']/following-sibling::dd").text

                # Bus Width - ميموري باص
                bus_width = driver.find_element(By.XPATH, "//dt[text()='Memory Bus']/following-sibling::dd").text
                
                # Boost Clock - بوست كلوك
                boost_clock = driver.find_element(By.XPATH, "//dt[text()='Boost Clock']/following-sibling::dd").text

                # Shading Units - عدد وحدات المعالجة
                shading_units = driver.find_element(By.XPATH, "//dt[text()='Shading Units']/following-sibling::dd").text

                # TDP - استهلاك الطاقة
                tdp = driver.find_element(By.XPATH, "//dt[text()='TDP']/following-sibling::dd").text

                # Bus Interface - إصدار الـ PCI
                pci = driver.find_element(By.XPATH, "//dt[text()='Bus Interface']/following-sibling::dd").text

                # Bandwidth - معدل نقل البيانات
                bandwidth = driver.find_element(By.XPATH, "//dt[text()='Bandwidth']/following-sibling::dd").text



                # file
                file_g = os.path.join(self.new_path, f"gpu_{name}.txt")
                with open(rf"{file_g}", "w") as file:
                    file.write(f"           == {all_name} ==               \n")
                    file.write(f"Architecture: {architecture}\n")
                    file.write(f"Process Size: {processor_size}\n")
                    file.write(f"Memory Size: {memory_size}\n")
                    file.write(f"Memory Type: {memory_type}\n")
                    file.write(f"Bus Width: {bus_width}\n")
                    file.write(f"Boost Clock: {boost_clock}\n")
                    file.write(f"Shading Units: {shading_units}\n")
                    file.write(f"TDB: {tdp}\n")
                    file.write(f"PCI: {pci}\n")
                    file.write(f"Bandwidth: {bandwidth}\n")
                    file.write("_"* 70)
            except:
                print("there is fail please try again")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        def m_board(self,name):
            driver.get("https://pcpartpicker.com/")

            try:
                search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav__search")))
                driver.execute_script("arguments[0].click();", search_button)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search_q']"))).send_keys("motherboard " +name + Keys.ENTER)

                item = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='search_results--link']/a"))).get_attribute('href')
                driver.switch_to.new_window("tab")
                driver.get(item)

                # Full Name
                f_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='pageTitle']"))).text

                # Socket CPU
                socket = driver.find_element(By.XPATH, "//h3[text()='Socket / CPU']/following-sibling::div").text
                
                # Size
                size = driver.find_element(By.XPATH, "//h3[text()='Form Factor']/following-sibling::div").text

                # Memory Max
                m_max = driver.find_element(By.XPATH, "//h3[text()='Memory Max']/following-sibling::div").text

                # Memory Type
                m_type = driver.find_element(By.XPATH, "//h3[text()='Memory Type']/following-sibling::div").text

                # Memory Slots
                m_slots = driver.find_element(By.XPATH, "//h3[text()='Memory Slots']/following-sibling::div").text

                # supported memory speeds
                s_memory = driver.find_element(By.XPATH, "//h3[text()= 'Memory Speed']/following-sibling::div").text

                # M.2 Slots
                try:
                    m2_slots = driver.find_element(By.XPATH, "//h3[text()='M.2 Slots']/following-sibling::div").text
                except:
                    m2_slots = None
                    

                # Sata Slots
                sata = driver.find_element(By.XPATH, "//h3[contains(text(),'SATA ')]/following-sibling::div/p").text


                # usb
                usb_key = driver.find_elements(By.XPATH, "//div[contains(@class, 'main-content')]//h3[contains(text(), 'USB')]")
                usb_value = driver.find_elements(By.XPATH, "//div[contains(@class,'main-content')]//h3[contains(text(), 'USB')]/following-sibling::div/p")


                # Wi=Fi
                wifi = driver.find_element(By.XPATH, "//h3[text()='Wireless Networking']/following-sibling::div/p").text

                file_m = os.path.join(self.new_path, f"m_{name}.txt")
                with open(rf"{file_m}", "w") as file:
                    file.write(f"       {f_name.upper()}\n")
                    file.write(f"Socket: {socket}\n")
                    file.write(f"Size: {size}\n")
                    file.write(f"Memory Max: {m_max}\n")
                    file.write(f"Memory Type: {m_type}\n")
                    file.write(f"Memory Slots: {m_slots}\n")
                    file.write(f"Supported Memory Speeds:\n{s_memory}\n")
                    file.write(f"M.2 slots: {m2_slots}\n")
                    file.write(f"Sata: {sata}\n")

                    # USB
                    for key, value in zip(usb_key, usb_value):
                        k_txt =  key.get_attribute('textContent').strip()
                        v_txt =  value.get_attribute('textContent').strip()
                        if k_txt:
                            file.write(f"{k_txt} ==> {v_txt}")

                    file.write(f"WiFi ==> {wifi}")

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                print("there is fail please try again")

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
                object.g_card(part_name)

            elif part_type == "mother board":
                part_name = input("write mother board name: ")
                object.m_board(part_name)

            elif part_type == "exit":
                break
            
            else:
                print("please recheck your character and try again")

        elif reorder =="n" :
            break
        
        else:
            print("please recheck your character and try again")

    if driver:
        try:
            driver.quit()
        except Exception:
            pass
    folders.start(object.new_path)


