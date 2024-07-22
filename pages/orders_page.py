import allure

from pages.base_page import BasePage
from data.urls import FEED_PAGE
from locators.orders_page_locators import *


class OrdersPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_orders_page(self):
        self.get_url(FEED_PAGE, ORDERS_TEXT)

    @allure.step('Проверка загрузки страницы профиля')
    def check_orders_page_load(self):
        self.check_url_loaded(FEED_PAGE, ORDERS_TEXT)

    @allure.step('Нажимаем на заказ')
    def click_order(self):
        self.click_on_element(ORDER_LINK)

    @allure.step('Проверка появления модального окна')
    def check_order_modal_window_appears(self):
        self.check_element_existence(ORDER_CART)

    @allure.step('Проверка существования заказа')
    def check_order_existence(self, number):
        self.check_element_existence(('xpath', f'//p[contains(text(), "{number}")]'))

    @allure.step('Получение счётчика заказов')
    def get_all_time_counter(self):
        return int(self.driver.find_element(*ALL_TIME_COUNTER).text)

    @allure.step('Получение счётчика заказов')
    def get_today_counter(self):
        return int(self.driver.find_element(*TODAY_COUNTER).text)

    @allure.step('Проверка номера заказа "В работе"')
    def check_number_in_work(self, number):
        ORDER_NUMBER = ('xpath', f'//ul[contains(@class, "OrderFeed_orderListReady")]//li[text()="{number}"]')
        assert self.driver.find_element(*ORDER_NUMBER)

