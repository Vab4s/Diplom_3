import time

import allure

from helpers.random_ingredient import random_ingredient, random_ingredient_and_counter
from pages.base_page import BasePage
from data.urls import MAIN_PAGE
from locators.main_page_locators import *


class MainPage(BasePage):

    @allure.step('Переход на главную страницу')
    def get_main_page(self):
        self.get_url(MAIN_PAGE, SECTION_CREATE_BURGER)



    @allure.step('Проверка загрузки главной страницы')
    def wait_main_page_load(self):
        self.wait_url_loading(SECTION_CREATE_BURGER)

    def click_make_order_button(self):
        self.click_on_element(BUTTON_MAKE_ORDER)

    def click_random_ingredient(self):
        ingredient = random_ingredient()
        self.click_on_element(ingredient)

    def click_modal_close_button(self):
        self.click_on_element(BUTTON_MODAL_CLOSE)

    @allure.step('Проверка загрузки главной страницы')
    def check_main_page_load(self):
        self.check_url_loaded(MAIN_PAGE, SECTION_CREATE_BURGER)

    def check_order_window_appears(self):
        self.check_element_existence(MODAL_SECTION_ORDER)





    def check_modal_section_appears(self):
        self.check_element_with_parameter_existence(MODAL_SECTION_INGREDIENT, 'class', 'Modal_modal_opened__3ISw4')

    def check_modal_section_disappears(self):
        self.check_element_unexistence(MODAL_SECTION_INGREDIENT)

    def create_order(self):
        source = random_ingredient()
        SOURCE = self.driver.find_element(*source)
        TARGET = self.driver.find_element(*CONSTRUCTOR_AREA)
        self.scroll_to_element(SOURCE)
        self.drug_and_drop_element(SOURCE, TARGET)
        self.click_make_order_button()
        self.check_element_existence(('xpath', '//img[@src="./static/media/tick.887b83be.gif"]'))


    def check_ingredient_counter(self):
        source, counter = random_ingredient_and_counter()
        SOURCE = self.driver.find_element(*source)
        TARGET = self.driver.find_element(*CONSTRUCTOR_AREA)
        self.scroll_to_element(SOURCE)
        self.drug_and_drop_element(SOURCE, TARGET)

        assert self.driver.find_element(*counter).text == '1'

