import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.locators import LOADING_GIF

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

    @allure.step(f'Переход на страницу')
    def get_url(self, url):
        self.driver.get(url)
        self.wait.until(expected_conditions.invisibility_of_element_located(LOADING_GIF))

    def wait_element(self, element):
        self.wait.until(expected_conditions.presence_of_element_located(element))

    @allure.step('Клик на элементе')
    def click_on_element(self, element):
        self.wait.until(expected_conditions.element_to_be_clickable(element)).click()
