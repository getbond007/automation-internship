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

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not shown in actual {actual_text}'

    def wait_to_be_clickable(self, *locator):
         self.driver.wait.until(
            EC.element_to_be_clickable(*locator),
             message=f'Element by {locator} not clickable'
         )

    def wait_for_element_to_appear(self, *locator):
            self.driver.wait.until(
                EC.visibility_of_element_located(locator),
                message=f'Element by {locator} did not appear'
            )

    def wait_for_element_to_disappear(self, *locator):
            self.driver.wait.until(
                EC.invisibility_of_element_located(locator),
                message=f'Element by {locator} still shown on the page'
            )

    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f'Expected URL {expected_url} but got {current_url}'

    def verify_partial_url(self, expected_partial_url):
        current_url = self.driver.current_url
        assert expected_partial_url in current_url, \
        f'Expected partial URL {expected_partial_url} not in {current_url}'

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f'Switching to window {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window {window_id}')
        self.driver.switch_to.window(window_id)

    def close(self):
        self.driver.close()