import allure
from selenium.webdriver.common.by import By


class HeaderPage:
    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    order_button_header = (By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text()="Заказать"]')
    cookie_button = (By.XPATH, './/button[text()="да все привыкли"]')

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажать logo «Яндекс» в хедере')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Нажать logo «Самокат» в хедере')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    # метод проверяет активна ли кнопка «Заказать» в хедере
    def check_header_order_button_enabled(self):
        return self.driver.find_element(*self.order_button_header).is_enabled()

    @allure.step('Нажать кнопку «Заказать» в хедере')
    def click_header_order_button(self):
        self.driver.find_element(*self.order_button_header).click()

    # метод кликает по кнопке «да все привыкли»
    @allure.step('Принять coockie')
    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()
