import requests
import allure
from data.endpoints import DELETE_USER


@allure.step('Удаление курьера')
@allure.description('"email" и "password" берутся из user_data, возвращаемого функцией регистрации юзера.')
def delete_user(userdata, token):
    payload = {"email": userdata[0], "password": userdata[1]}
    requests.delete(DELETE_USER, data=payload, headers={"Authorization": token})
