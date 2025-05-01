from pages.base_page import Page
from pages.home_page import HomePage
from pages.login_page import LogInPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.secondary_deals_page import SecondaryPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.home_page = HomePage(driver)
        self.login_page = LogInPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.secondary_deals_page = SecondaryPage(driver)