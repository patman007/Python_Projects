from selenium import webdriver
import time
import unittest

#Use the below imports for command line to get Line 11 to Line 12 to work
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..", ".."))

#Import the login and home page
from Selenium.POM_Html.Pages.loginPage import LoginPage
from Selenium.POM_Html.Pages.homePage import HomePage

#Add HTML Reports
import HtmlTestRunner

#Unit Test Class
class LoginTest(unittest.TestCase):


    @classmethod  #Class Function
    def setUpClass(cls):
        #Webdriver path and make sure to use '/' for the folder paths instead of '\'
        cls.driver = webdriver.Chrome(executable_path="C:/Users/patri/Desktop/Python_Projects/Selenium/POM_Html/drivers/chromedriver.exe")
        #cls.driver = webdriver.Chrome('..\drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        home.page.click_welcome()
        homepage.click_logout()

        #Find the elements by id at beginning of project and comment out later
        # self.driver.find_element_by_id('txtUsername').send_keys("Admin")
        # self.driver.find_element_by_id('txtPassword').send_keys("admin123")
        # self.driver.find_element_by_id('btnLogin').click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text('Logout').click()
        #Time out
        self.time.sleep(2)


    def test_02login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials123")
        self.time.sleep(2)


    @classmethod #Class Function
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed successfully")

if __name__ == '__main__':
    #Webdriver path and make sure to use '/' for the folder paths instead of '\'
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/patri/Desktop/Python_Projects/Selenium/POM_Html/reports'))
