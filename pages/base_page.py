import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from locators.general_locators import *
from locators.nav_menu_locators import *

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    @allure.step(f'Переход на страницу')
    def get_url(self, url, element):
        self.driver.get(url)
        self.wait.until(expected_conditions.invisibility_of_element_located(LOADING_GIF))   # Завершение анимации
        self.wait.until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Проверка загрузки страницы')
    def check_url_loaded(self, url, element):   # element - эдемент страницы, который должен быть загружен
        self.wait.until(expected_conditions.invisibility_of_element_located(LOADING_GIF))   # Завершение анимации
        self.wait.until(expected_conditions.visibility_of_element_located(element))
        assert (self.driver.current_url == url and self.driver.find_element(*element))

    @allure.step('Существование эдемента с определённым значением параметра')
    def check_element_with_parameter_existence(self, element, attribute, parameter):
        assert parameter in self.wait.until(expected_conditions.visibility_of_element_located(element)).get_attribute(attribute)

    @allure.step('Существование элемента')
    def check_element_existence(self, element):
        assert self.wait.until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Несуществование элемента')
    def check_element_unexistence(self, element):
        assert self.wait.until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик на элементе')
    def click_on_element(self, element):
        self.wait.until(expected_conditions.element_to_be_clickable(element)).click()

    @allure.step('Перетаскивание элемента')
    def drug_and_drop_element(self, source, target):
        self.action.click_and_hold(source).pause(1).move_to_element(target).pause(1).release().perform()

    @allure.step('Ввод данных в поле input')
    def fill_input_field(self, element, text):
        self.wait.until(expected_conditions.visibility_of_element_located(element)).send_keys(text)

    @allure.step('Проверка того, что поле input активно')
    def check_input_field_is_active(self, element):
        assert 'input_status_active' in self.driver.find_element(*element).get_attribute('class')



    # Nav-меню
    @allure.step('Клик а пункт меню Конструктор')
    def click_constructor_menu(self):
        self.click_on_element(BUTTON_CONSTRUCTOR)

    @allure.step('Клик а пункт меню Лента заказов')
    def click_orders_menu(self):
        self.click_on_element(BUTTON_ORDERS)

    @allure.step('Клик а пункт меню логотип Stellar Burgers')
    def click_logo_menu(self):
        self.click_on_element(BUTTON_LOGO)

    @allure.step('Клик а пункт меню Личный кабинет')
    def click_account_menu(self):
        self.click_on_element(BUTTON_ACCOUNT)
