import allure

from pages.base_page import BasePage
from data.urls import ORDERS_PAGE
from locators.orders_page_locators import *


class OrdersPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_orders_page(self):
        self.get_url(ORDERS_PAGE, ORDERS_TEXT)

    @allure.step('Проверка загрузки страницы профиля')
    def check_orders_page_load(self):
        self.check_url_loaded(ORDERS_PAGE, ORDERS_TEXT)