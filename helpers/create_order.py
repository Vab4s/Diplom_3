import random
import allure
import requests
from data.ingredients import ingredients_id

@allure.step('Создание списка ингредиентов')
def create_order_list():
    burger = list()
    for ingredient in range(3):
        burger.append(random.choice(ingredients_id))
    return {"ingredients": burger}


@allure.step('Запрос создания заказа')
def send_create_order_post_request(access_token):
    payload = create_order_list()
    order_response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload, headers={"Authorization": access_token})
    return order_response.json()['order']['number']