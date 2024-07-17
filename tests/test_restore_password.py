import time

import allure

from pages.login_page import LoginPage
from pages.restore_pass_page import RestorePassPage
from pages.reset_password_page import ResetPassPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@allure.story('Проверка восстановления пароля')
class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления при нажатии на "Восстановить пароль"')
    def test_click_restore_password(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.click_restore_password_button()

        restore_pass_page = RestorePassPage(driver)
        restore_pass_page.check_restore_pass_page_load()

    @allure.title('Проверка перехода на страницу восстановления при нажатии на "Восстановить пароль"')
    def test_enter_mail_and_click_restore(self, driver):
        restore_pass_page = RestorePassPage(driver)
        restore_pass_page.get_restore_pass_page()
        restore_pass_page.fill_email('qweqwe@qweqwe.qwe')
        restore_pass_page.click_restore_button()

        reset_pass_page = ResetPassPage(driver)
        reset_pass_page.check_reset_pass_page_load()
