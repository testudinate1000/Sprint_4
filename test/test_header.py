import allure
from selenium import webdriver

from page_object import header
from page_object import yandex_page
from page_object import main_page
from page_object import order_page


class TestHeader:
    driver = None
    url = main_page.MainPage.url

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка работы кнопки логотипа «Самоката»')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_click_on_scooter_logo_open_scooter_page(self):
        self.driver.maximize_window()
        self.driver.get(order_page.OrderPage.url)

        page = header.HeaderPage(self.driver)
        page.click_scooter_logo()

        page = main_page.MainPage(self.driver)

        assert page.url == self.driver.current_url

    @allure.title('Проверка работы кнопки логотипа «Яндекс»')
    @allure.description('Если нажать на логотип «Яндекс», попадёшь на главную страницу «Яндекс».')
    def test_click_on_yandex_logo_open_yandex_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        page = header.HeaderPage(self.driver)
        page.click_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        yandex = yandex_page.YandexPage(self.driver)

        assert yandex.url == self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
