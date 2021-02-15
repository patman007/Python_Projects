from Selenium.POM_Html.Locators.locators import Locators

class HomePage():
    #Create a constructor using def __init(self)
    #This is necessary to use for constructors
    def __init__(self, driver):

        #Any changes with the code can be done here since we have the constructors working dynamically
        #Using Page Object Model (POM)
        self.driver = driver
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"

    #Click Welcome Function
    def click_welcome_(self):
        self.driver.find_elements_by_id(self.welcome_link_id).click()

    #Click Logout Function
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

#Any changes with the code can be done here since we have the constructors working dynamically
#Using Page Object Model (POM)