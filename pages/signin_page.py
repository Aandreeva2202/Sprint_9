import allure

from locators.signin_page_locators import SigninPageLocators
from pages.base_page import BasePage


class SigninPage(BasePage):

    @allure.step('Дождаться загрузки страницы авторизации')
    def wait_for_load(self):
        self.find_visible_element(SigninPageLocators.TITLE)

    @allure.step('Проверить отображение формы авторизации')
    def is_signin_form_displayed(self):
        return self.is_element_visible(SigninPageLocators.FORM)

    @allure.step('Заполнить форму авторизации')
    def fill_signin_form(self, login, password):
        # Стенд авторизует по имени пользователя, которое вводится в поле «Электронная почта»
        self.fill_input(SigninPageLocators.LOGIN_INPUT, login)
        self.fill_input(SigninPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажать кнопку «Войти» в форме')
    def click_submit_button(self):
        self.click_element(SigninPageLocators.SUBMIT_BUTTON)

    def login(self, login, password):
        self.wait_for_load()
        self.fill_signin_form(login, password)
        self.click_submit_button()
