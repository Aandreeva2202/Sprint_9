import allure

from urls import MAIN_PAGE_URL, RECIPES_PAGE_URL


@allure.feature('Авторизация')
class TestAuthorization:

    @allure.title('После авторизации открывается главная страница и отображается кнопка «Выход»')
    def test_authorization_redirects_to_main_page(self, main_page, signin_page, registered_user):
        main_page.open(MAIN_PAGE_URL)
        main_page.click_signin_button()
        signin_page.login(registered_user['username'], registered_user['password'])
        main_page.wait_for_load()

        assert main_page.get_current_url() == RECIPES_PAGE_URL and main_page.is_logout_button_displayed()
