import allure

from pages.base_page import BasePage
from data.urls import RESTORE_PASSWORD_PAGE
from locators.general_locators import *
from locators.restore_password_page_locators import *

class RestorePassPage(BasePage):
    @allure.step('Переход на страницу восстановления пароля')
    def get_restore_pass_page(self):
        self.get_url(RESTORE_PASSWORD_PAGE, BUTTON_RESTORE)

    @allure.step('Проверка загрузки страницы восстановления пароля')
    def check_restore_pass_page_load(self):
        self.check_url_loaded(RESTORE_PASSWORD_PAGE, BUTTON_RESTORE)

    @allure.step('Заполнение поля e-mail')
    def fill_email(self, email):
        self.fill_input_field(INPUT_EMAIL, email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_on_element(BUTTON_RESTORE)