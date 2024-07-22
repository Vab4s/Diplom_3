import allure

from pages.base_page import BasePage
from data.urls import PROFILE_PAGE
from locators.profile_page_locators import *

class ProfilePage(BasePage):

    @allure.step('Проверка загрузки страницы профиля')
    def wait_profile_page_load(self):
        self.wait_url_loading(BUTTON_PROFILE_SAVE)

    @allure.step('Переход на страницу профиля')
    def get_profile_page(self):
        self.get_url(PROFILE_PAGE, BUTTON_PROFILE_SAVE)

    @allure.step('Проверка загрузки страницы профиля')
    def check_profile_page_load(self):
        self.check_url_loaded(PROFILE_PAGE, BUTTON_PROFILE_SAVE)

    @allure.step('Клин на пункт история заказов')
    def click_orders_history(self):
        self.click_on_element(LINK_ORDERS_HISTORY)

    @allure.step('Клин на пункт Выйти')
    def click_exit(self):
        self.click_on_element(LINK_EXIT)
