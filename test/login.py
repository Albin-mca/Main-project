from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
print("Login test case started")
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
driver.find_element("xpath", "/html/body/header/section/div/div/div[3]/div/div/div/a[1]").click()
time.sleep(3)
driver.find_element("name", "email").send_keys("albingeorgework284@gmail.com")
time.sleep(3)
driver.find_element("name", "password").send_keys("1234")
time.sleep(3)
driver.find_element("xpath", "/html/body/section/div/div/form/div[4]/button").click()
time.sleep(3)
print("User Logged In")

driver.find_element("xpath", "/html/body/header/section/div/div/a[2]").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/section[2]/div/div/main/div/div[1]/figure/figcaption/a").click()
time.sleep(3)

driver.find_element("xpath", "/html/body/section/div/div[1]/div/main/form/article/div[3]/div/select/option[2]").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/section/div/div[1]/div/main/form/article/div[4]/div/select/option[2]").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/section/div/div[1]/div/main/form/article/button/span").click()
time.sleep(3)
print("Added to Cart")

# driver.find_element("xpath", "/html/body/section/div/div/aside[1]/div/table/tbody/tr/td[2]/div/div/div[2]/form/button/i").click()
# time.sleep(3)
# print("Increased Product")

# driver.find_element("xpath", "/html/body/section/div/div/aside[1]/div/table/tbody/tr/td[4]/a").click()
# time.sleep(3)
# print("Remove Product")

driver.find_element("xpath", "/html/body/header/section/div/div/div[3]/div/div/div/a[2]").click()
time.sleep(3)
# print("Logout")



