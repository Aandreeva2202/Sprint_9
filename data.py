from pathlib import Path

# Корневая директория проекта — папка, в которой лежит этот файл
APP_DIR = Path(__file__).parent

USER_FIRST_NAME = 'Иван'
USER_LAST_NAME = 'Тестов'
USER_PASSWORD = 'Sprint9Pass!'

RECIPE_INGREDIENT = 'сахар'
RECIPE_INGREDIENT_AMOUNT = '100'
RECIPE_COOKING_TIME = '15'
RECIPE_DESCRIPTION = 'Смешать все ингредиенты и подавать к столу.'
RECIPE_IMAGE_PATH = APP_DIR / 'assets' / 'recipe.png'
