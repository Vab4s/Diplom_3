import allure

from pages.base_page import BasePage

from data.urls import RESTORE_PASSWORD_PAGE
from locators.locators import INPUT_EMAIL, BUTTON_RESTORE

class RestorePassPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def get_restore_pass_page(self):
        RESTORE = ('xpath', '//h2[text()="Восстановление пароля"]')
        self.get_url(RESTORE_PASSWORD_PAGE, RESTORE)

    @allure.step('Проверка загрузки страницы восстановления пароля')
    def check_restore_pass_page_load(self):
        self.check_url_loaded(RESTORE_PASSWORD_PAGE, INPUT_EMAIL)

    @allure.step('Заполнение поля e-mail')
    def fill_email(self, email):
        self.fill_input_field(INPUT_EMAIL, email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_on_element(BUTTON_RESTORE)