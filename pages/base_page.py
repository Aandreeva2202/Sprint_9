import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_present_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill_input(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def upload_file(self, locator, file_path):
        # input[type='file'] скрыт на странице, поэтому ждём только его наличия в DOM
        self.find_present_element(locator).send_keys(file_path)

    def get_element_text(self, locator):
        return self.find_visible_element(locator).text

    def is_element_visible(self, locator):
        try:
            return self.find_visible_element(locator).is_displayed()
        except TimeoutException:
            return False

    @staticmethod
    def format_locator(locator, value):
        method, selector = locator
        return method, selector.format(value)
