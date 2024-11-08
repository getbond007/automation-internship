from pages.base_page import Page
from pages.home_page import HomePage
from pages.login_page import LogInPage
from pages.off_plan_page import OffPlanPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.home_page = HomePage(driver)
        self.login_page = LogInPage(driver)
        self.off_plan_page = OffPlanPage(driver)