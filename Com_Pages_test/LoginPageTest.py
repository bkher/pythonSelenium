
from selenium import webdriver
from Com_Pages.LoginPage import loginpage
from Com_Pages.HomePage import homepage
from Com_Pages.ContactUs_Page import contactUsPage
from Com_Pages.GiftCard_page import GiftCardPage
from Com_Pages.Cart_Page import cartPage
from UtilityPackage.Utility import utility
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
        login = loginpage(driver)
        ReadExcel = utility
        login.click_login_path()
        login.click_loginLink_button()
        login.enter_username(ReadExcel.readExcel(self,1, 1))
        login.enter_password(ReadExcel.readExcel(self,1, 2))
        login.click_login_button()
        time.sleep(3)
        driver.save_screenshot("login done.png")
        
        homepagevar = homepage(driver)
        
        homepagevar.clik_contacUS()
        contactpage = contactUsPage(driver)
        contactpage.helpcentertext()
        contactpage.orderrelatedQuesryLink()
        contactpage.NonOrderRelatedQuesry()
        contactpage.FrequentlyAsledQuestions()
        contactpage.Order_button()
        driver.save_screenshot("Contact Us Page.png")
        time.sleep(3)
        
        driver.back()
        
        homepagevar.click_GiftCard()
        giftpage = GiftCardPage(driver)
        giftpage.sendGiftCardText()
        giftpage.browseGiftcardText()
        giftpage.ListOfOccassionsText()
        giftpage.ReceviedGiftcardText()
        time.sleep(3)
        driver.save_screenshot("Gift Card Page.png")
        driver.back()
        
        homepagevar.Click_Cart()
        CartPage = cartPage(driver)
        CartPage.bag_text()
        CartPage.Delivery_text()
        CartPage.Payment_text()
        CartPage.Needhelp_text()
        CartPage.Secure_text()
        time.sleep(3)
        driver.save_screenshot("Cart Page.png")
        driver.back()
       
        time.sleep(3)
        login.click_login_path()
        homepagevar.click_logout()
        driver.save_screenshot("logout done.png")
        
        
        
    @classmethod
    def tearDown(cls):
        time.sleep(5)
        cls.driver.close()
        print("completed")

    

 




        