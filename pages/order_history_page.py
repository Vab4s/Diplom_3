import allure

from pages.base_page import BasePage
from data.urls import ORDER_HISTORY_PAGE


class OrderHistoryPage(BasePage):

    def get_order_number(self):
        NUMBER = ('xpath', '//div[@class="OrderHistory_textBox__3lgbs mb-6"]/child::p[contains(@class, "text_type_digits-default")]')
        order_number = self.driver.find_element(*NUMBER).text
        return order_number

    @allure.step('Проверка загрузки страницы профиля')
    def check_orders_history_page_load(self):
        content_box = ('xpath', '//div[@class="Account_contentBox__2CPm3"]')
        self.check_url_loaded(ORDER_HISTORY_PAGE, content_box)