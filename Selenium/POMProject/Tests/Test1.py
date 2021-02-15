from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Another way to do a relative file path
# driver = webdriver.Chrome(r'C:\Users\patri\Desktop\Python_Projects\Selenium\POMProject\drivers\chromedriver.exe')
#Correct way to do a relative path
driver = webdriver.Chrome('..\drivers\chromedriver.exe')

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step.")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
print('Test completed successfully')
driver.quit() # or drive.close()

