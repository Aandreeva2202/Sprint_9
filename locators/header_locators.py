from selenium.webdriver.common.by import By


class HeaderLocators:
    SIGNIN_LINK = (By.XPATH, "//header//a[text()='Войти']")
    SIGNUP_LINK = (By.XPATH, "//header//a[text()='Создать аккаунт']")
    CREATE_RECIPE_LINK = (By.XPATH, "//header//a[text()='Создать рецепт']")
    LOGOUT_BUTTON = (By.XPATH, "//header//a[text()='Выход']")
