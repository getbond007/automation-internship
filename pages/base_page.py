from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def wait_to_be_clickable(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
             message=f'Element by {locator} not clickable'
         )

    def wait_for_element_to_appear(self, *locator):
            self.driver.wait.until(
                EC.visibility_of_element_located(locator),
                message=f'Element by {locator} did not appear'
            )
