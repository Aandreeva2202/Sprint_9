import allure

from urls import MAIN_PAGE_URL, SIGNIN_PAGE_URL


@allure.feature('Создание аккаунта')
class TestRegistration:

    @allure.title('После регистрации открывается страница авторизации и отображается форма авторизации')
    def test_registration_redirects_to_signin_page(self, main_page, signup_page, signin_page, new_user):
        main_page.open(MAIN_PAGE_URL)
        main_page.click_signup_button()
        signup_page.register(new_user)
        signin_page.wait_for_load()

        assert signin_page.get_current_url() == SIGNIN_PAGE_URL and signin_page.is_signin_form_displayed()
