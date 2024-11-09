from pages.base_page import Page

class HomePage(Page):

    #Open the main page
    def open_home(self):
        self.open('https://soft.reelly.io/sign-in')