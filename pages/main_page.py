import allure

from helpers.random_ingredient import random_ingredient, random_ingredient_and_counter
from pages.base_page import BasePage
from data.urls import MAIN_PAGE
from locators.main_page_locators import *


class MainPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_main_page(self):
        self.get_url(MAIN_PAGE, SECTION_CREATE_BURGER)

    @allure.step('Проверка загрузки страницы профиля')
    def check_main_page_load(self):
        self.check_url_loaded(MAIN_PAGE, SECTION_CREATE_BURGER)

    def click_make_order_button(self):
        self.click_on_element(BUTTON_MAKE_ORDER)

    def check_order_window_appears(self):
        self.check_element_existence(MODAL_SECTION_ORDER)

    def click_random_ingredient(self):
        ingredient = random_ingredient()
        self.click_on_element(ingredient)

    def click_modal_close_button(self):
        self.click_on_element(BUTTON_MODAL_CLOSE)

    def check_modal_section_appears(self):
        self.check_element_with_parameter_existence(MODAL_SECTION_INGREDIENT, 'class', 'Modal_modal_opened__3ISw4')

    def check_modal_section_disappears(self):
        self.check_element_unexistence(MODAL_SECTION_INGREDIENT)

    # def move_random_ingredient_to_basket(self):
    #
    #     SOURCE = self.driver.find_element(*random_ingredient())
    #     TARGET = self.driver.find_element(*CONSTRUCTOR_AREA)
    #     self.scroll_to_element(SOURCE)
    #     self.action.drag_and_drop(SOURCE, TARGET)


    def check_ingredient_counter(self):
        source, counter = random_ingredient_and_counter()
        SOURCE = self.driver.find_element(*source)
        TARGET = self.driver.find_element(*CONSTRUCTOR_AREA)
        self.scroll_to_element(SOURCE)
        self.drug_and_drop_element(SOURCE, TARGET)

        assert self.driver.find_element(*counter).text == '1'

