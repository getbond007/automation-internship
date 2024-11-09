from pages.base_page import Page
from selenium.webdriver.common.by import By

class LogInPage(Page):

    EMAIL_ID = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".login-button")

    #Sign in to main page
    def sing_in(self,userid,password):
        self.input_text(userid, *self.EMAIL_ID)
        self.input_text(password, *self.PASSWORD)
        self.wait_for_element_to_appear(*self.CONTINUE_BUTTON)
        self.click(*self.CONTINUE_BUTTON)