import os

import pytest
from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.file_detector import LocalFileDetector

from helpers import generate_recipe, generate_user
from pages.create_recipe_page import CreateRecipePage
from pages.main_page import MainPage
from pages.recipe_page import RecipePage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from urls import MAIN_PAGE_URL


@pytest.fixture
def driver():
    selenoid_uri = os.getenv('SELENOID_URI')
    if selenoid_uri:
        # Запуск в Docker Compose: подключаемся к Selenoid.
        # Версия браузера и его настройки задаются в browsers.json
        driver = webdriver.Remote(command_executor=selenoid_uri, options=webdriver.ChromeOptions())
        # Selenoid принимает файлы на /session/{id}/file, а Selenium 4 по умолчанию шлёт на /se/file
        driver.file_detector = LocalFileDetector()
        driver.command_executor.add_command(Command.UPLOAD_FILE, 'POST', '/session/$sessionId/file')
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)


@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)


@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)


@pytest.fixture
def recipe_page(driver):
    return RecipePage(driver)


@pytest.fixture
def new_user():
    return generate_user()


@pytest.fixture
def new_recipe():
    return generate_recipe()


@pytest.fixture
def registered_user(main_page, signup_page, signin_page, new_user):
    main_page.open(MAIN_PAGE_URL)
    main_page.click_signup_button()
    signup_page.register(new_user)
    signin_page.wait_for_load()
    return new_user


@pytest.fixture
def authorized_user(main_page, signin_page, registered_user):
    signin_page.login(registered_user['username'], registered_user['password'])
    main_page.wait_for_load()
    return registered_user
