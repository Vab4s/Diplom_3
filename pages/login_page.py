import allure

from pages.base_page import BasePage
from data.urls import LOGIN_PAGE
from locators.general_locators import *
from locators.login_page_locators import *


class LoginPage(BasePage):
    @allure.step('Переход на страницу входа в аккаунт')
    def get_login_page(self):
        self.get_url(LOGIN_PAGE, BUTTON_ENTER)

    @allure.step('Клик на ссылку "Восстановление пароля"')
    def click_restore_password_button(self):
        self.click_on_element(LINK_RESTORE_PASSWORD)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_visibe_button(self):
        self.click_on_element(BUTTON_VISIBLE_PASSWORD)

    @allure.step('Заполнение поля email')
    def fill_email(self, email):
        self.fill_input_field(INPUT_EMAIL, email)

    @allure.step('Заполнение поля password')
    def fill_password(self, password):
        self.fill_input_field(INPUT_PASSWORD, password)

    @allure.step('Нажать на кнопку Войти')
    def click_enter_button(self):
        self.click_on_element(BUTTON_ENTER)

    @allure.step('Логин')
    def fill_data_and_login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_enter_button()


    @allure.step('Проверка активности поля password')
    def check_password_field_is_active(self):
        self.check_input_field_is_active(DIV_PASSWORD)

    @allure.step('Проверка загрузки страницы хода в аккаунт')
    def check_login_page_load(self):
        self.check_url_loaded(LOGIN_PAGE, DIV_PASSWORD)




