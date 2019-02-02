from Locators.ElementLocators import locators
from selenium.webdriver.common.action_chains import ActionChains

class loginpage:
    
    def __init__(self, driver):
        self.driver = driver
        self.login_click_xpath = locators.login_click_xpath
        self.username_textbox_xpath = locators.username_textbox_xpath
        self.password_textbox_xpath = locators.password_textbox_xpath
        self.login_button_xpath = locators.login_button_xpath
        self.login_Link_xpath = locators.login_Link_xpath

    def click_login_path(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.login_click_xpath)).perform()
    
    def click_loginLink_button(self):
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(self.login_Link_xpath)).perform()
              
    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    