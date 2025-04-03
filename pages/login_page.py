import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.google.com/"

    signeinbtn = (By.XPATH, "//a[@aria-label='Sign in']")
    USERNAME_FIELD  = (By.XPATH, "//input[@aria-label='Email or phone']")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    #DASHBOARD_INDICATOR = (By.ID, "dashboard")

    def open_login_page(self):
        self.open_url(self.URL)


    def login(self, username, password):
        self.click(self.signeinbtn)
        self.wait()
        self.click(self.USERNAME_FIELD)
        self.enter_text(self.USERNAME_FIELD, username)
        self.send_enter_key(self.USERNAME_FIELD)  # Press Enter after entering username
        self.wait()
        time.sleep(3)
        # Take screenshot after username input
        self.take_screenshot("username_entered")

        self.enter_text(self.PASSWORD_FIELD, password)
        #self.click(self.LOGIN_BUTTON)


    #def is_dashboard_displayed(self):
        #return self.find_element(self.DASHBOARD_INDICATOR).is_displayed()
