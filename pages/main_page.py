import allure

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать кнопку «Создать аккаунт» в шапке')
    def click_signup_button(self):
        self.click_element(HeaderLocators.SIGNUP_LINK)

    @allure.step('Нажать кнопку «Войти» в шапке')
    def click_signin_button(self):
        self.click_element(HeaderLocators.SIGNIN_LINK)

    @allure.step('Перейти на таб «Создать рецепт»')
    def click_create_recipe_tab(self):
        self.click_element(HeaderLocators.CREATE_RECIPE_LINK)

    @allure.step('Дождаться загрузки главной страницы со списком рецептов')
    def wait_for_load(self):
        self.find_visible_element(MainPageLocators.TITLE)

    @allure.step('Проверить отображение кнопки «Выход»')
    def is_logout_button_displayed(self):
        return self.is_element_visible(HeaderLocators.LOGOUT_BUTTON)
