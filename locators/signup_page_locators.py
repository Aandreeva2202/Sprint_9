from selenium.webdriver.common.by import By


class SignupPageLocators:
    TITLE = (By.XPATH, "//main//h1[text()='Регистрация']")
    FIRST_NAME_INPUT = (By.XPATH, "//main//form//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//main//form//input[@name='last_name']")
    USERNAME_INPUT = (By.XPATH, "//main//form//input[@name='username']")
    EMAIL_INPUT = (By.XPATH, "//main//form//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//main//form//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//main//form//button[text()='Создать аккаунт']")
