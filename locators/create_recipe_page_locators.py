from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    TITLE = (By.XPATH, "//main//h1[text()='Создание рецепта']")
    NAME_INPUT = (By.XPATH, "//label[div[text()='Название рецепта']]/input")
    INGREDIENT_INPUT = (By.XPATH, "//label[div[text()='Ингредиенты']]/input")
    # Вариант из выпадающего списка ингредиентов, {} — точное название
    INGREDIENT_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'ingredientsInputs')]"
        "/div[contains(@class, 'container')]/div[text()='{}']",
    )
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    # Добавленный в рецепт ингредиент, {} — точное название
    ADDED_INGREDIENT = (
        By.XPATH,
        "//div[contains(@class, 'ingredientsAdded')]//span[text()='{}']",
    )
    COOKING_TIME_INPUT = (By.XPATH, "//label[div[text()='Время приготовления']]/input")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//label[div[text()='Описание рецепта']]/textarea")
    IMAGE_FILE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//main//form//button[text()='Создать рецепт']")
