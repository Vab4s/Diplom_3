import requests
import allure
import random
import string
from data.endpoints import POST_CREATE_USER

@allure.step('Регистрация нового пользователя')
def create_user():

    def generate_random_string(length=9):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Список, в который будут переданы сгенерированные данные пользователя
    user_data = []

    # Генерируем емаил, пароль и имя пользователя
    email = f'{generate_random_string(10)}@{generate_random_string(5)}.{generate_random_string(3)}'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {"email": email, "password": password, "name": name}

    # Отправляем запрос на регистрацию и сохраняем ответ в переменную response
    response = requests.post(POST_CREATE_USER, data=payload)

    # Если регистрация прошла успешно (код ответа 200), добавляем в список емаил и пароль пользователя
    if response.status_code == 200:
        user_data.append(email)
        user_data.append(password)
        user_data.append(name)

    # Возвращаем регистрационные данные
    return user_data, response.json()
