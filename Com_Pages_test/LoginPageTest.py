
from selenium import webdriver
from Com_Pages.LoginPage import loginpage
from Com_Pages.HomePage import homepage
from Com_Pages.ContactUs_Page import contactUsPage
from Com_Pages.GiftCard_page import GiftCardPage
import unittest
import time
from selenium.webdriver.common.keys import Keys


class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\Bhagi\\Downloads\\chromedriver_win32\\chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://www.myntra.com")
      #  driver.send_keys(Keys.ESCAPE)
        login = loginpage(driver)
        login.click_login_path()
        login.click_loginLink_button()
        login.enter_username("bgtkher002@gmail.com")
        login.enter_password("bgt@BGT123")
        login.click_login_button()
        time.sleep(3)
        
        
        homepagevar = homepage(driver)
        homepagevar.clik_contacUS()
        '''
        driver.back()
        
        driver.back()
        homepagevar.Click_Cart()
        driver.back()
        
        login.click_login_path()
        homepagevar.click_logout()
        time.sleep(3)
        '''
        contactpage = contactUsPage(driver)
        
        contactpage.helpcentertext()
        
        contactpage.orderrelatedQuesryLink()
        contactpage.NonOrderRelatedQuesry()
        contactpage.FrequentlyAsledQuestions()
        contactpage.Order_button()
        driver.back()
        homepagevar.click_GiftCard()
        
        giftpage = GiftCardPage(driver)
        giftpage.sendGiftCardText()
        giftpage.browseGiftcardText()
        giftpage.ListOfOccassionsText()
        giftpage.ReceviedGiftcardText()
        driver.back()
        
        
        
        
    @classmethod
    def tearDown(cls):
        time.sleep(5)
        cls.driver.close()
        print("completed")

    

 




        