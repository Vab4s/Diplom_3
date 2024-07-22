import allure

from helpers.create_user import create_user
from helpers.delete_user import delete_user
from helpers.create_order import send_create_order_post_request
from pages.orders_page import OrdersPage


class TestOrderFeed:
    @classmethod
    @allure.title('Создание пользователя')
    def setup_class(cls):
        cls.user_data, cls.response_text = create_user()
        cls.email, cls.password, cls.name = cls.user_data
        cls.access_token = cls.response_text['accessToken']

    @allure.title('Проверка клика на заказ')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        orders_page.click_order()
        orders_page.check_order_modal_window_appears()

    @allure.title('Проверка появления заказа в ленте')
    def test_orders_in_history_are_in_feed(self, driver):
        order_id = send_create_order_post_request(self.access_token)
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        orders_page.check_order_existence(order_id)

    @allure.title('Проверка увеличения счётчика заказов за всё время')
    def test_all_time_counter_increase(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        all_time_counter_before = orders_page.get_all_time_counter()
        send_create_order_post_request(self.access_token)
        all_time_counter_after = orders_page.get_all_time_counter()

        assert all_time_counter_after == all_time_counter_before + 1

    @allure.title('Проверка увеличения счётчика заказов за сегодняшний день')
    def test_today_counter_increase(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        today_counter_before = orders_page.get_today_counter()
        send_create_order_post_request(self.access_token)
        today_counter_after = orders_page.get_today_counter()

        assert today_counter_after == today_counter_before + 1

    @allure.title('Проверка появления номера заказа "в работе"')
    def test_order_number_in_work(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.get_orders_page()
        order_id = send_create_order_post_request(self.access_token)
        orders_page.check_number_in_work(order_id)

    @classmethod
    @allure.title('Удаление созданного пользователя')
    def teardown_class(cls):
        delete_user(cls.user_data, cls.access_token)
