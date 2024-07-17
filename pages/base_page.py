import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.locators import LOADING_GIF

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step(f'Переход на страницу')
    def get_url(self, url, element):
        self.driver.get(url)
        self.wait.until(expected_conditions.invisibility_of_element_located(LOADING_GIF))
        self.wait.until(expected_conditions.visibility_of_element_located(element))

    def check_url_loaded(self, url, element):
        self.wait.until(expected_conditions.visibility_of_element_located(element))
        assert (self.driver.current_url == url and self.driver.find_element(*element))

    @allure.step('Клик на элементе')
    def click_on_element(self, element):
        self.wait.until(expected_conditions.element_to_be_clickable(element)).click()

    @allure.step('Ввод данных в поле input')
    def fill_input_field(self, element, text):
        self.wait.until(expected_conditions.visibility_of_element_located(element)).send_keys(text)

    def wait_load_element(self, element):
        self.wait.until(expected_conditions.visibility_of_element_located(element))