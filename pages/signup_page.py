import allure

from locators.signup_page_locators import SignupPageLocators
from pages.base_page import BasePage


class SignupPage(BasePage):

    @allure.step('Дождаться загрузки страницы регистрации')
    def wait_for_load(self):
        self.find_visible_element(SignupPageLocators.TITLE)

    @allure.step('Заполнить форму регистрации')
    def fill_signup_form(self, user):
        self.fill_input(SignupPageLocators.FIRST_NAME_INPUT, user['first_name'])
        self.fill_input(SignupPageLocators.LAST_NAME_INPUT, user['last_name'])
        self.fill_input(SignupPageLocators.USERNAME_INPUT, user['username'])
        self.fill_input(SignupPageLocators.EMAIL_INPUT, user['email'])
        self.fill_input(SignupPageLocators.PASSWORD_INPUT, user['password'])

    @allure.step('Нажать кнопку «Создать аккаунт» в форме')
    def click_submit_button(self):
        self.click_element(SignupPageLocators.SUBMIT_BUTTON)

    def register(self, user):
        self.wait_for_load()
        self.fill_signup_form(user)
        self.click_submit_button()
