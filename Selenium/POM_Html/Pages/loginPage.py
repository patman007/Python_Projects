from Selenium.POM_Html.Locators.locators import Locators

class LoginPage():
    #Create a constructor using def __init(self)
    #This is necessary to use for constructors
    def __init__(self, driver):
        self.driver = driver

        #Any changes with the code can be done here since we have the constructors working dynamically
        #Using Page Object Model (POM)
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

        #Alternate method later on using locator.py for above
        # self.username_textbox_id = Locators.username_textbox_id
        # self.password_textbox_id = Locators.password_textbox_id
        # self.login_button_id = Locators.welcome_link_id

    #Username Function
    def enter_username(self, username):
        self.driver.find_elements_by_id(self.username_textbox_id).clear()
        self.driver.find_elements_by_id(self.username_textbox_id).send_keys(username)

    #Password Function
    def enter_password(self, password):
        self.driver.find_elements_by_id(self.password_textbox_id).clear()
        self.driver.find_elements_by_id(self.password_textbox_id).send_keys(password)

    #Login Button Function
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    #Login Button Function
    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.click_invalid_username_message).text
        return msg



