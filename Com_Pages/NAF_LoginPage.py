from Locators.ElementLocators import locators
import selenium
class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.Enter_UserName=locators.Enter_UserName
        self.Enter_Password=locators.Enter_Password
        self.Click_Login=locators.Click_Login
        self.WelcomeBack_text=locators.WelcomeBack_text
        self.OtherText=locators.OtherText

    def enterUsername(self,username):
        ele = self.driver.find_element_by_xpath(self.Enter_UserName).is_displayed()
        assert  ele ==True
        self.driver.find_element_by_xpath(self.Enter_UserName).send_keys(username)

    def enterPassword(self,password):
        ele = self.driver.find_element_by_xpath(self.Enter_Password).is_displayed()

        assert ele == True
        self.driver.find_element_by_xpath(self.Enter_Password).send_keys(password)

    def clickLoginButton(self):
        ele = self.driver.find_element_by_xpath(self.Click_Login).is_displayed()
        assert ele == True
        self.driver.find_element_by_xpath(self.Click_Login).click()

    def VerifyLoginPageText(self):
        ele = self.driver.find_element_by_xpath(self.WelcomeBack_text).is_displayed()

        if (ele == True):
            print("Welcome back text is present")
        else:
            print("Welcome back text is not present")
        ele1 = self.driver.find_element_by_xpath(self.OtherText).is_displayed()
        
        if (ele1 == True):
            print("Other text is present")
        else:
            print("Other text is not present")
