import time

import allure

from pages.login_page import LoginPage
from data.urls import RESTORE_PASSWORD_PAGE

@allure.story('Проверка восстановления пароля')
class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления при нажатии на "Восстановить пароль"')
    def test_click_restore_password(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.click_restore_password()
        assert driver.current_url == RESTORE_PASSWORD_PAGE
