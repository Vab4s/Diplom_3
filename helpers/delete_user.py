import requests
import allure
from data.endpoints import DELETE_USER


@allure.step('Удаление пользователя')
def delete_user(userdata, token):
    payload = {"email": userdata[0], "password": userdata[1]}
    requests.delete(DELETE_USER, data=payload, headers={"Authorization": token})
