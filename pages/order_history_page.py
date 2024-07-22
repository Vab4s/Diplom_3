import allure

from pages.base_page import BasePage
from data.urls import ORDER_HISTORY_PAGE


class OrderHistoryPage(BasePage):
    @allure.step('Проверка загрузки страницы профиля')
    def check_orders_history_page_load(self):
        content_box = ('xpath', '//div[@class="Account_contentBox__2CPm3"]')
        self.check_url_loaded(ORDER_HISTORY_PAGE, content_box)