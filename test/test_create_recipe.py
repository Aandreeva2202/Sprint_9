import allure


@allure.feature('Создание рецепта')
class TestCreateRecipe:

    @allure.title('После создания рецепта отображается его карточка и введённое название')
    def test_create_recipe_shows_recipe_card(
            self, main_page, create_recipe_page, recipe_page, authorized_user, new_recipe):
        main_page.click_create_recipe_tab()
        create_recipe_page.create_recipe(new_recipe)

        assert recipe_page.is_recipe_card_displayed() and recipe_page.get_recipe_title() == new_recipe['name']
