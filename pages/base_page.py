import time

from selenium.webdriver import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def send_enter_key(self, locator):
        self.find_element(locator).send_keys(Keys.RETURN)

    def wait(self):
        self.driver.implicitly_wait(10)

    def take_screenshot(self, screenshot_name="screenshot"):
        """Take a screenshot and save it with a timestamp."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_filename = f"{screenshot_name}_{timestamp}.png"
        self.driver.get_screenshot_as_file(screenshot_filename)
        print(f"Screenshot saved as {screenshot_filename}")
