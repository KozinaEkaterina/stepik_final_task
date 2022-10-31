from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator, locator_value):
        try:
            self.browser.find_element(locator, locator_value)
        except NoSuchElementException:
            return False
        return True
