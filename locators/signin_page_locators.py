from selenium.webdriver.common.by import By


class SigninPageLocators:
    TITLE = (By.XPATH, "//main//h1[text()='Войти на сайт']")
    FORM = (By.XPATH, "//main//form[.//button[text()='Войти']]")
    LOGIN_INPUT = (By.XPATH, "//main//form//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//main//form//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//main//form//button[text()='Войти']")
