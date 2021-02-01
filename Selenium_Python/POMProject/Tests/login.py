from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase)

driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe")

driver.implicity_wait(10)
driver.maximize_window

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_Keys("Admin")

driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

driver.find_element_by_id("welcome").click()

driver.find_element_by_link_text("Logout").click()
time.sleep(2)

driver.close()
driver.quit()
print('Test Completed')