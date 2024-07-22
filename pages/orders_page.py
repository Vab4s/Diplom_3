import allure

from pages.base_page import BasePage
from data.urls import ORDERS_PAGE
from locators.orders_page_locators import *




from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrdersPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_orders_page(self):
        self.get_url(ORDERS_PAGE, ORDERS_TEXT)

    @allure.step('Проверка загрузки страницы профиля')
    def check_orders_page_load(self):
        self.check_url_loaded(ORDERS_PAGE, ORDERS_TEXT)

    @allure.step('Нажимаем на заказ')
    def click_order(self):
        self.click_on_element(ORDER_LINK)

    def check_order_modal_window_appears(self):
        self.check_element_existence(ORDER_CART)

    def check_order_existence(self, number):
        self.check_element_existence(('xpath', f'//p[contains(text(), "{number}")]'))

    def get_all_time_counter(self):
        return int(self.driver.find_element(*ALL_TIME_COUNTER).text)

    def get_today_counter(self):
        return int(self.driver.find_element(*TODAY_COUNTER).text)

    def check_number_in_work(self, number):
        order = ('xpath', f'/html/body/div/div/main/div/div/div/div[1]/ul[2]/li[text()="{number}"]')
        assert self.driver.find_element(*order)

