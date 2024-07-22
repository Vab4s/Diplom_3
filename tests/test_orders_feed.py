import requests

import allure
from helpers.create_user import create_user
from helpers.delete_user import delete_user
from helpers.create_order import send_create_order_post_request

from pages.orders_page import OrdersPage


class TestOrderFeed:
    @classmethod
    def setup_class(cls):
        cls.user_data, cls.response_text = create_user()
        cls.email, cls.password, cls.name = cls.user_data
        cls.access_token = cls.response_text['accessToken']

    @allure.step('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        orders_page.click_order()
        orders_page.check_order_modal_window_appears()

    def test_orders_in_history_are_in_feed(self, driver):
        # payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa79"]}
        # order = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload, headers={"Authorization": self.access_token})
        # order_id = order_1.json()['order']['number']

        order_id = send_create_order_post_request(self.access_token)
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        orders_page.check_order_existence(order_id)

    def test_all_time_counter_increase(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        all_time_counter_before = orders_page.get_all_time_counter()
        # payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa79"]}
        # requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload,
        #                         headers={"Authorization": self.access_token})

        send_create_order_post_request(self.access_token)
        all_time_counter_after = orders_page.get_all_time_counter()

        assert all_time_counter_after == all_time_counter_before + 1

    def test_today_counter_increase(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        today_counter_before = orders_page.get_today_counter()
        # payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa79"]}
        # requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload,
        #                         headers={"Authorization": self.access_token})
        send_create_order_post_request(self.access_token)
        today_counter_after = orders_page.get_today_counter()
        assert today_counter_after == today_counter_before + 1

    def test_order_number_in_work(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        # payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa79"]}
        # order = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload,
        #               headers={"Authorization": self.access_token})
        order_id = send_create_order_post_request(self.access_token)
        orders_page.check_number_in_work(order_id)



    @classmethod
    @allure.title('Удаление созданного пользователя')
    def teardown_class(cls):
        delete_user(cls.user_data, cls.access_token)