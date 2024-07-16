import allure

from pages.base_page import BasePage

from data.urls import LOGIN_PAGE
from locators.locators import LINK_RESTORE_PASSWORD
class LoginPage(BasePage):

    @allure.step('Переход на страницу входа в аккаунт')
    def get_login_page(self):
        self.get_url(LOGIN_PAGE)

    @allure.step('Клик на ссылку "Восстановление пароля"')
    def click_restore_password(self):
        self.click_on_element(LINK_RESTORE_PASSWORD)


