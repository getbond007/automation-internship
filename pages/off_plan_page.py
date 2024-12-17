from pages.base_page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

class OffPlanPage(Page):

    OFF_PLAN_MENU = (By.XPATH, "//a[@class='menu-text-link-leaderboard w--current']")
    SALES_STATUS = (By.CSS_SELECTOR,"#Location-2")
    OUT_OF_STOCK_STATUS = (By.XPATH, "//div[@class='_5-comission']")
    OFF_PLAN_TITLE = (By.CSS_SELECTOR,"div.page-title.off_plan")

    FILTER_ICON = (By.CSS_SELECTOR, 'a .filter-text')
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//a[text()="Apply filter"]')

    CARDS_MIN_PRICE = (By.CSS_SELECTOR, '[wized="projectMinimumPrice"]')

    #Select the off plan menu option
    def click_on_off_plan(self):
        self.wait_for_element_to_appear(*self.OFF_PLAN_MENU)
        self.wait_to_be_clickable(*self.OFF_PLAN_MENU)

    #Verify that correct page is opened
    def verify_off_plan(self):
        self.wait_for_element_to_appear(*self.OFF_PLAN_TITLE)
        expected_title = "Total projects"
        self.verify_text(expected_title, *self.OFF_PLAN_TITLE)

    #Select out of stock option from the dropdown
    def select_status_out_of_stocks(self):
        sales_status_dropdown = Select(self.find_element(*self.SALES_STATUS))
        sales_status_dropdown.select_by_value('Out of stock')

    #Verify if sales status is displaying as expected for selected filter
    def verify_out_of_stocks(self):
        # Find all sales status elements
        self.wait_for_element_to_appear(*self.OUT_OF_STOCK_STATUS)

        statuses = self.find_elements(*self.OUT_OF_STOCK_STATUS)
        #Expectd Status
        expected_text = "Out of stock"

        # Loop through each sales status and check if it has 'out of stock' text
        for status in statuses:
            # Find the text containing the 'out of stock' text within each sales
            actual_text = status.find_element(*self.OUT_OF_STOCK_STATUS).text
            assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

    def filter_products_by_price(self):
        self.wait_for_element_to_appear(*self.FILTER_ICON)
        self.click(*self.FILTER_ICON)
        self.input_text(1200000,*self.FILTER_PRICE_FROM)
        self.input_text(2000000, *self.FILTER_PRICE_TO)
        self.click(*self.APPLY_FILTER_BUTTON)

    def verify_price_in_cards(self):
        # Find all card price elements
        self.wait_for_element_to_appear(*self.CARDS_MIN_PRICE)

        minPrices = self.find_elements(*self.CARDS_MIN_PRICE)

        # Loop through each cards price
        for price in minPrices:
            # Find the price of each card and compare with expected
            actual_price = int(price.text.replace('AED','').replace(' ','').replace(',',''))
            assert  1200000 < actual_price < 2000000, f'Actual price {actual_price} did not fall between 1200000 and 2000000'
