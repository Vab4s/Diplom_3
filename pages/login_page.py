import allure

from pages.base_page import BasePage
from data.urls import LOGIN_PAGE
from locators.locators import LINK_RESTORE_PASSWORD

class LoginPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_login_page(self):
        ENTER = ('xpath', '//h2[text()="Вход"]')
        self.get_url(LOGIN_PAGE, ENTER)

    @allure.step('Клик на ссылку "Восстановление пароля"')
    def click_restore_password_button(self):
        self.click_on_element(LINK_RESTORE_PASSWORD)


