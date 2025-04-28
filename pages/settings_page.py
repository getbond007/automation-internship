from operator import truediv
from time import sleep

from selenium.common import NoSuchElementException

from pages.base_page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class SettingsPage(Page):

    SETTINGS_MENU = (By.XPATH, "//div[@class='settings-code w-embed']")
    SETTINGS_IMG = (By.XPATH, "//src[@class='image-profile-settings']")
    CONNECT_THE_COMPANY = (By.XPATH, "//a[@class='button-link-menu w-inline-block']")
    SETTINGS_OPTION_CLIENT_MODE = (By.XPATH, "//div[@class='page-setting-block client-mode']")
    SETTINGS_OPTIONS = (By.XPATH, "//a[@class='page-setting-block w-inline-block']")

    #click on settings
    def click_on_settings(self):
        self.wait_to_be_clickable(*self.SETTINGS_MENU)
        self.click(*self.SETTINGS_MENU)

    #Verify that correct page is opened
    def verify_settings_page(self):
        actual_link = self.driver.current_url
        expected_link = "https://soft.reelly.io/settings"
        self.verify_actual_text(expected_link, actual_link)

    #Verify there are 13 options for the settings
    def verify_settings_option(self):
        options = self.find_elements(*self.SETTINGS_OPTIONS)
        option_client_mode = self.find_elements(*self.SETTINGS_OPTION_CLIENT_MODE)

        i=len(options) + len(option_client_mode)

        expected_text = 'Settings has 13 Options available'

        if i!=13:
            self.verify_actual_text('Settings has 13 Options not available', expected_text)
    
    #verify connect the company is visible
    def verify_connect_the_company_option(self):

        companies = self.find_elements(*self.CONNECT_THE_COMPANY)
        self.wait_to_be_clickable(*self.CONNECT_THE_COMPANY)

        expected_text = 'Connect the company'
        found_company_text = 'false'

        for company in companies:
            # Find the text containing the 'Connect the company' text within each company field
            actual_text = company.text
            if actual_text == expected_text:
                found_company_text = 'Connect the company'

        self.verify_actual_text('Connect the company',found_company_text)