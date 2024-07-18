import allure

from helpers.create_user import create_user
from helpers.delete_user import delete_user

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage

class TestAccount:
    @classmethod
    def setup_class(cls):
        cls.user_data, cls.response_text = create_user()
        cls.email, cls.password, cls.name = cls.user_data
        cls.access_token = cls.response_text['accessToken']

    def test_click_account_button_without_authorization(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.check_main_page_load()
        main_page.click_account_menu()

        login_page = LoginPage(driver)
        login_page.check_login_page_load()

    def test_click_account_button_with_authorization(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.fill_data_and_login(self.email, self.password)

        main_page = MainPage(driver)
        main_page.check_main_page_load()
        main_page.click_account_menu()

        profile_page = ProfilePage(driver)
        profile_page.check_profile_page_load()

    def test_click_orders_story_with_authorization(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.fill_data_and_login(self.email, self.password)

        main_page = MainPage(driver)
        main_page.check_main_page_load()
        main_page.click_account_menu()

        profile_page = ProfilePage(driver)
        profile_page.check_profile_page_load()
        profile_page.click_orders_history()

        orders_history_page = OrderHistoryPage(driver)
        orders_history_page.check_orders_history_page_load()

    def test_click_exit_account(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.fill_data_and_login(self.email, self.password)

        main_page = MainPage(driver)
        main_page.check_main_page_load()
        main_page.click_account_menu()

        profile_page = ProfilePage(driver)
        profile_page.check_profile_page_load()
        profile_page.click_exit()

        login_page = LoginPage(driver)
        login_page.check_login_page_load()

    @classmethod
    @allure.title('Удаление созданного пользователя')
    def teardown_class(cls):
        delete_user(cls.user_data, cls.access_token)
