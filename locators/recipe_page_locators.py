from selenium.webdriver.common.by import By


class RecipePageLocators:
    RECIPE_CARD = (By.XPATH, "//main//div[contains(@class, 'single-card') and img]")
    RECIPE_TITLE = (By.XPATH, "//main//h1[contains(@class, 'single-card__title')]")
