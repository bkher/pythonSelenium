from Locators.ElementLocators import locators
from _ast import Return

class GiftCardPage:
    def __init__(self, driver):
        self.driver = driver
        self.SendGiftCard_text_xpath = locators.SendGiftCard_text_xpath
        self.browser_giftCard_text_xpath = locators.browser_giftCard_text_xpath
        self.ListOfOccasionsBrowse_texts_xpath = locators.ListOfOccasionsBrowse_texts_xpath
        self.ReceivedGifCard_Text_xpath = locators.ReceivedGifCard_Text_xpath
       
    def sendGiftCardText(self):
        ele = self.driver.find_element_by_xpath(self.SendGiftCard_text_xpath).is_displayed()
        assert ele == True
        #print('send gift card text is displayed= ',self.driver.find_element_by_xpath(self.SendGiftCard_text_xpath).is_displayed())
        
    def browseGiftcardText(self):
        ele = self.driver.find_element_by_xpath(self.browser_giftCard_text_xpath).is_displayed()
        assert ele == True
        #print('Browse gift card text is displayed= ', self.driver.find_element_by_xpath(self.browser_giftCard_text_xpath).is_displayed())
        
    def ListOfOccassionsText(self):
        occassations=[]
        ele = self.driver.find_elements_by_xpath(self.ListOfOccasionsBrowse_texts_xpath).text
        occassations.append(ele)
        occasations1 = ["Wedding","Season's Greetings","Birthday","Look Good","Anniversary","Welcome","Best Wishes","Congrats","Good Luck","Best Mom","Best Dad"]

        for i in occassations:
            for j in occasations1:
                if i==j:
                    break
                
    def ReceviedGiftcardText(self):
        ele = self.driver.find_element_by_xpath(self.ReceivedGifCard_Text_xpath).is_displayed()
        assert ele == True
        #print('Received gift card text is displayed= ', self.driver.find_element_by_xpath(self.ReceivedGifCard_Text_xpath).is_displayed())
        
        