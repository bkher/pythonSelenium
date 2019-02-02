from Locators.ElementLocators import locators
from selenium.webdriver.common.action_chains import ActionChains

class homepage:
    def __init__(self, driver):
        self.driver = driver
        self.contactUs_xpath = locators.contactUs_xpath
        self.GiftCard_xpath = locators.GiftCard_xpath
        self.Cart_xpath = locators.Cart_xpath
        self.logout_xpath = locators.logout_xpath
        self.myntra_logo_link=locators.myntra_logo_link


    def clik_contacUS(self):
        self.driver.find_element_by_xpath(self.contactUs_xpath).click()

    def click_GiftCard(self):
        self.driver.find_element_by_xpath(self.GiftCard_xpath).click()

    def Click_Cart(self):
        self.driver.find_element_by_xpath(self.Cart_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
        
    def Click_myntra_Logo(self):
        self.driver.find_element_by_xpath(self.myntra_logo_link).click()