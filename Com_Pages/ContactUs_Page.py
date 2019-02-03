from Locators.ElementLocators import locators

class contactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpcenter_Text_Xpath = locators.helpcenter_Text_Xpath
        self.OrderRelatedQuery_link_xpath = locators.OrderRelatedQuery_link_xpath
        self.NonOrderRelatedIssue_link_xpath = locators.NonOrderRelatedIssue_link_xpath
        self.FrequentlyAskedQuestons_link_Xpat = locators.FrequentlyAskedQuestons_link_Xpat
        self.Order_link_xpath = locators.Order_link_xpath

    def helpcentertext(self):
        ele = self.driver.find_element_by_xpath(self.helpcenter_Text_Xpath).text
        assert ele == "HELP CENTER"
        #print ('help Center text is displayed = ',self.driver.find_element_by_xpath(self.helpcenter_Text_Xpath).is_displayed())
        
    def orderrelatedQuesryLink(self):
        ele = self.driver.find_element_by_xpath(self.OrderRelatedQuery_link_xpath).is_enabled()
        assert ele == True
        #print ('order related queries link is enable= ',self.driver.find_element_by_xpath(self.OrderRelatedQuery_link_xpath).is_enabled())

    def NonOrderRelatedQuesry(self):
        ele = self.driver.find_element_by_xpath(self.NonOrderRelatedIssue_link_xpath).is_enabled()
        assert ele ==True
        #print('Non order related query is enable= ',self.driver.find_element_by_xpath(self.NonOrderRelatedIssue_link_xpath).is_enabled())

    def FrequentlyAsledQuestions(self):
        ele = self.driver.find_element_by_xpath(self.FrequentlyAskedQuestons_link_Xpat).is_displayed()
        assert ele == True
        #print('frequently asked question is displayed=  ',self.driver.find_element_by_xpath(self.FrequentlyAskedQuestons_link_Xpat).is_displayed())

    def Order_button(self):
        ele = self.driver.find_element_by_xpath(self.Order_link_xpath).is_enabled()
        assert ele == True
        #print('order button is enable=  ',self.driver.find_element_by_xpath(self.Order_link_xpath).is_enabled())
        
