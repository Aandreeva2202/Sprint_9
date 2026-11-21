import allure

from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class RecipePage(BasePage):

    @allure.step('Проверить отображение карточки рецепта')
    def is_recipe_card_displayed(self):
        return self.is_element_visible(RecipePageLocators.RECIPE_CARD)

    @allure.step('Получить название рецепта из карточки')
    def get_recipe_title(self):
        return self.get_element_text(RecipePageLocators.RECIPE_TITLE)
