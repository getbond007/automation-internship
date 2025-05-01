from operator import truediv
from time import sleep

from selenium.common import NoSuchElementException

from pages.base_page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class SecondaryPage(Page):

    SECONDARY_MENU = (By.LINK_TEXT, "Secondary")
    FILTER = (By.XPATH, "//div[@class='filter-button']")
    FILTER_PRODUCTS = (By.XPATH, "//div[@wized='ListingTypeBuy']")
    APPLY_BUTTON = (By.XPATH, "//a[@class='button-filter w-button']")
    FOR_SALE = (By.XPATH, "//div[@wized='saleTagMLS']")

    NEXT_PAGE = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
    TOTAL_NUMBER_OF_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')

    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    LISTING_PRICE = (By.CSS_SELECTOR, '[wized="unitPriceMLS"]')

    #click on settings
    def click_on_secondary(self):
        self.wait_to_be_clickable(*self.SECONDARY_MENU)
        self.click(*self.SECONDARY_MENU)

    #Verify that correct page is opened
    def verify_secondary_page(self):
        actual_link = self.driver.current_url
        expected_link = "https://soft.reelly.io/secondary-listings"
        self.verify_actual_text(expected_link, actual_link)

    #Click on filter option
    def click_on_filter(self):
        self.wait_to_be_clickable(*self.FILTER)
        self.click(*self.FILTER)

    #Filter the products by “want to buy”
    def filter_by_products(self):
        self.click(*self.FILTER)
        #self.wait_to_be_clickable(*self.FILTER_PRODUCTS)
        self.click(*self.FILTER_PRODUCTS)
        self.wait_to_be_clickable(*self.APPLY_BUTTON)
        self.click(*self.APPLY_BUTTON)

    def filter_by_price(self):
        self.click(*self.FILTER)
        self.input_text(1200000,*self.FILTER_PRICE_FROM)
        self.input_text(2000000, *self.FILTER_PRICE_TO)
        self.wait_to_be_clickable(*self.APPLY_BUTTON)
        self.click(*self.APPLY_BUTTON)

    def verify_each_secondary_listings(self,filter_type):

        #Get total number of pagination or child pages
        #We need to loop each page and assert all projects in each page
        total_number_of_pages = int(self.find_element(*self.TOTAL_NUMBER_OF_PAGES).text)

        # To keep track of next page opening or not
        page_increment = 0

        # Then Loop through each page
        while total_number_of_pages >= 1:
            # Reduce the total number of pages so that loop will end after going through all pages
            total_number_of_pages = total_number_of_pages - 1

            # Keep track if clicking "Next" is actually taking to right page number
            page_increment = page_increment + 1

            try:
                self.wait_for_element_to_appear(*self.CURRENT_PAGE_COUNT)
                # Find what is current page number
                current_page_num = int(self.find_element(*self.CURRENT_PAGE_COUNT).text)
                # Assert if that is the correct page number
                assert current_page_num == page_increment, f'Expected Page Number {current_page_num} is not matching with Actual Page Number {page_increment}'

                # Reuse method call to assert the actual ask
                SecondaryPage.verify_filter_type(self,filter_type)

                # Move to next page
                self.find_element(*self.NEXT_PAGE).click()

            except NoSuchElementException:
                print(f'Next Page number {page_increment} not available or required element not present')
            else:
                print(f'Finished Page Number : {page_increment}')

    def verify_filter_type(self, filter_type):
        # assert the fist page before looping through rest all pages
        if filter_type == "LISTING_TYPE":
            SecondaryPage.verify_each_listing(self)
        elif filter_type == "PRICE_RANGE":
            SecondaryPage.verify_price_range(self)

    def verify_each_listing(self):
        for_sales = self.find_elements(*self.FOR_SALE)

        for sale in for_sales:
            title = sale.text
            self.verify_actual_text("Want to buy",title)

    def verify_price_range(self):
        # Find card price for all elements
        self.wait_for_element_to_appear(*self.LISTING_PRICE)
        min_prices = self.find_elements(*self.LISTING_PRICE)

        # Loop through each card price
        for price in min_prices:
            # Find the price of each card and compare with expected
            price_text = price.text.replace('AED','').replace(' ','').replace(',','')
            actual_price = int(price_text)
            assert  1200000 < actual_price < 2000000, f'Actual price {actual_price} did not fall between 1200000 and 2000000'