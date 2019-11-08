from selenium import webdriver
from Com_Pages.NAF_LoginPage import LoginPage
from UtilityPackage.Utility import utility
import unittest
import time


class LoginPagetest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\Bhagi\\Downloads\\chromedriver_win32 _78\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://docitt-naf.lender.qa.lendfoundry.com/")
        login = LoginPage(driver)
        ReadExcel = utility
        time.sleep(8)
        driver.save_screenshot('F:\\EclipsePractice\\PythonSelenium\\Screenshots\\LoginPage.png')
        login.VerifyLoginPageText()
        login.enterUsername(ReadExcel.readExcel(self, 2, 1))
        login.enterPassword(ReadExcel.readExcel(self, 2, 2))
        login.clickLoginButton()
        time.sleep(8)
        if (driver.current_url == "http://docitt-naf.lender.qa.lendfoundry.com/#/pipeline"):
            print("login succeesul")
        driver.save_screenshot("F:\\EclipsePractice\\PythonSelenium\\Screenshots\\LoginDone.png")





