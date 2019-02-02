class locators:
    #login object

    myntra_logo_link ="//*[@id='desktop-header-cnt']/div[2]/div[1]/a"
    login_click_xpath = "//*[@id='desktop-header-cnt']/div[2]/div[2]/div/div[1]"
    # login_Link_xpath ="//a[text()='login']"
    login_Link_xpath = "//*[@id='desktop-header-cnt']/div[2]/div[2]/div/div[2]/div[2]/div[2]/a[2]"
    username_textbox_xpath = "//input[@name='email']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//button[text()='Log in']"
    

    #homepage object

    contactUs_xpath = "//*[@id='desktop-header-cnt']/div[1]/a[text()='Contact Us']"
    GiftCard_xpath = "//*[@id='desktop-header-cnt']/div[1]/a[text()='Gift Card']"
    Cart_xpath = "//*[@id='desktop-header-cnt']/div[2]/div[2]/a/span[1]"
    logout_xpath = "//div[text()=' Logout ']"

    
    #Contact us Page
    
    helpcenter_Text_Xpath = "//div[text()='HELP CENTER']"
    OrderRelatedQuery_link_xpath = "//div[text()='Order Related Queries']"
    NonOrderRelatedIssue_link_xpath = "//div[text()='Non-order Related Issues']"
    FrequentlyAskedQuestons_link_Xpat = "//div[text()='Frequently Asked Questions']"
    Order_link_xpath = "//button[text()='ORDERS']"
    
    
    #gift Card Page
    
    SendGiftCard_text_xpath = "//button[text()='SEND GIFT CARD']"
    browser_giftCard_text_xpath = "//div[text()='Browse Gift Cards By Occasions']"
    ListOfOccasionsBrowse_texts_xpath = "//*[@id='mountRoot']/div/div/div[4]/div[2]/div[2]/div/div[1]/div/div"
    ReceivedGifCard_Text_xpath = "//div[text()='Received a gift card?']"
    
    
    #Cart Page 
    
    bag_text_xpath = "//li[text()='BAG']"
    Delivery_text_xpath = "//li[text()='DELIVERY']"
    Payment_text_xpath = "//li[text()='PAYMENT']"
    SecureText_text_xpath = "//div[text()='100% SECURE']"
    NeedHelpContactUs_text_Xpath = "//span[contains(text(),'Need Help ? Contact Us')]"
    