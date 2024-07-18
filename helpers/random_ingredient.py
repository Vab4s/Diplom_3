import random
from locators.main_page_locators import INGREDIENT

def random_ingredient():
    method, path = INGREDIENT
    number = random.randint(1, 15)
    path = f'({path}){[number]}'
    return (method, path)

def random_ingredient_and_counter():
    method, path = INGREDIENT
    number = random.randint(3, 15)
    path = f'({path}){[number]}'
    counter = path + '//p[contains(@class, "counter_counter__num")]'
    return (method, path), (method, counter)