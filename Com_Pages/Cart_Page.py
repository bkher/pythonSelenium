from Locators.ElementLocators import locators
class cartPage:
    def __init__(self, driver):
        self.driver = driver
        self.bag_text_xpath = locators.bag_text_xpath
        self.Delivery_text_xpath = locators.Delivery_text_xpath
        self.Payment_text_xpath = locators.Payment_text_xpath
        self.SecureText_text_xpath = locators.SecureText_text_xpath
        self.NeedHelpContactUs_text_Xpath=locators.NeedHelpContactUs_text_Xpath


    def bag_text(self):
        ele = self.driver.find_element_by_xpath(self.bag_text_xpath).is_displayed()
        assert ele == True
        #print('bag text is displyed= ',self.driver.find_element_by_xpath(self.bag_text_xpath).is_displayed())

    def Delivery_text(self):
        ele = self.driver.find_element_by_xpath(self.Delivery_text_xpath).is_displayed()
        assert ele == True
        #print('deliery text is displyed= ',self.driver.find_element_by_xpath(self.Delivery_text_xpath).is_displayed())
    
    def Payment_text(self):
        ele = self.driver.find_element_by_xpath(self.Payment_text_xpath).is_displayed()
        assert ele == True
        #print('Payment text is displyed= ',self.driver.find_element_by_xpath(self.Payment_text_xpath).is_displayed())

    def Secure_text(self):
        ele = self.driver.find_element_by_xpath(self.SecureText_text_xpath).text
        assert ele == "100% SECURE"
        #print('100% secure text is displyed= ',self.driver.find_element_by_xpath(self.SecureText_text_xpath).is_displayed())
    
    def Needhelp_text(self):
        ele = self.driver.find_element_by_xpath(self.NeedHelpContactUs_text_Xpath).is_displayed()
        assert ele == True
        #print('Need helpcontact us text is displyed= ',self.driver.find_element_by_xpath(self.NeedHelpContactUs_text_Xpath).is_displayed())
