import allure

from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):

    @allure.step('Дождаться загрузки страницы создания рецепта')
    def wait_for_load(self):
        self.find_visible_element(CreateRecipePageLocators.TITLE)

    @allure.step('Ввести название рецепта: {name}')
    def fill_name(self, name):
        self.fill_input(CreateRecipePageLocators.NAME_INPUT, name)

    @allure.step('Добавить ингредиент «{ingredient}» в количестве {amount}')
    def add_ingredient(self, ingredient, amount):
        self.fill_input(CreateRecipePageLocators.INGREDIENT_INPUT, ingredient)
        option = self.format_locator(CreateRecipePageLocators.INGREDIENT_OPTION, ingredient)
        self.click_element(option)
        self.fill_input(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)
        added = self.format_locator(CreateRecipePageLocators.ADDED_INGREDIENT, ingredient)
        self.find_visible_element(added)

    @allure.step('Ввести время приготовления: {minutes}')
    def fill_cooking_time(self, minutes):
        self.fill_input(CreateRecipePageLocators.COOKING_TIME_INPUT, minutes)

    @allure.step('Ввести описание рецепта')
    def fill_description(self, description):
        self.fill_input(CreateRecipePageLocators.DESCRIPTION_TEXTAREA, description)

    @allure.step('Загрузить фото рецепта')
    def upload_image(self, image_path):
        self.upload_file(CreateRecipePageLocators.IMAGE_FILE_INPUT, image_path)

    @allure.step('Нажать кнопку «Создать рецепт»')
    def click_submit_button(self):
        self.click_element(CreateRecipePageLocators.SUBMIT_BUTTON)

    def create_recipe(self, recipe):
        self.wait_for_load()
        self.fill_name(recipe['name'])
        self.add_ingredient(recipe['ingredient'], recipe['amount'])
        self.fill_cooking_time(recipe['cooking_time'])
        self.fill_description(recipe['description'])
        self.upload_image(recipe['image_path'])
        self.click_submit_button()
