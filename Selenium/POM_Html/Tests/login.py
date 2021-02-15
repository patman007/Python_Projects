from selenium import webdriver
import time
import unittest

#Unit Test Class
class LoginTest(unittest.TestCase):

    @classmethod  #Class Function
    def setUpClass(cls):
        #Webdriver path
        cls.driver = webdriver.Chrome(executable_path="C:/Users/patri/Desktop/Python_Projects/Selenium/POM_Html/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        #Find the elements by id
        self.driver.find_element_by_id('txtUsername').send_keys("Admin")
        self.driver.find_element_by_id('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text('Logout').click()
        #Time out
        self.time.sleep(2)

    @classmethod #Class Function
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed successfully")



