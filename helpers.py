import random
import string

from data import (
    RECIPE_COOKING_TIME,
    RECIPE_DESCRIPTION,
    RECIPE_IMAGE_PATH,
    RECIPE_INGREDIENT,
    RECIPE_INGREDIENT_AMOUNT,
    USER_FIRST_NAME,
    USER_LAST_NAME,
    USER_PASSWORD,
)


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_user():
    suffix = generate_random_string(10)
    return {
        'first_name': USER_FIRST_NAME,
        'last_name': USER_LAST_NAME,
        'username': f'user{suffix}',
        'email': f'user{suffix}@example.com',
        'password': USER_PASSWORD,
    }


def generate_recipe():
    return {
        'name': f'Рецепт {generate_random_string(8)}',
        'ingredient': RECIPE_INGREDIENT,
        'amount': RECIPE_INGREDIENT_AMOUNT,
        'cooking_time': RECIPE_COOKING_TIME,
        'description': RECIPE_DESCRIPTION,
        'image_path': str(RECIPE_IMAGE_PATH),
    }
