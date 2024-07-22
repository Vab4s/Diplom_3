import allure

from pages.base_page import BasePage
from data.urls import RESET_PASSWORD_PAGE
from locators.reset_page_locators import *


class ResetPassPage(BasePage):

    @allure.step('Переход на страницу сброса пароля')
    def get_reset_pass_page(self):
        self.get_url(RESET_PASSWORD_PAGE, BUTTON_SAVE)

    @allure.step('Проверка загрузки страницы сброса пароля')
    def check_reset_pass_page_load(self):
        self.check_url_loaded(RESET_PASSWORD_PAGE, INPUT_NEW_PASSWORD)
