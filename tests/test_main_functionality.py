import allure

from helpers.create_user import create_user
from helpers.delete_user import delete_user
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_page import OrdersPage

class TestMainFunctionality:
    @classmethod
    def setup_class(cls):
        cls.user_data, cls.response_text = create_user()
        cls.email, cls.password, cls.name = cls.user_data
        cls.access_token = cls.response_text['accessToken']

    def test_click_constructor_button(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.click_constructor_menu()

        main_page = MainPage(driver)
        main_page.check_main_page_load()

    def test_click_orders_button(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_orders_menu()

        orders_page = OrdersPage(driver)
        orders_page.check_orders_page_load()

    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_random_ingredient()
        main_page.check_modal_section_appears()

    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_random_ingredient()
        main_page.click_modal_close_button()
        main_page.check_modal_section_disappears()

    def test_counter_ingredients_increase(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.check_ingredient_counter()

    def test_authorized_user_can_make_order(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.fill_data_and_login(self.email, self.password)

        main_page = MainPage(driver)
        main_page.check_main_page_load()
        main_page.click_make_order_button()
        main_page.check_order_window_appears()

    @classmethod
    @allure.title('Удаление созданного пользователя')
    def teardown_class(cls):
        delete_user(cls.user_data, cls.access_token)
