from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    EMAIL_ID = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR,".login-button")

    #Open the main page
    def open_main(self):
        self.open('https://soft.reelly.io')

    #Sign in to main page
    def sing_in(self,userid,password):
        self.input_text(userid, *self.EMAIL_ID)
        self.input_text(password, *self.PASSWORD)
        self.click(*self.CONTINUE_BUTTON)