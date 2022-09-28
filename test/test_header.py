import allure

from page_object.header import HeaderPage
from page_object import yandex_page
from page_object.main_page import MainPage
from page_object.order_page import OrderPage


class TestHeader:
    driver = None
    url = MainPage.url

    @allure.title('Проверка работы кнопки логотипа «Самоката»')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_click_on_scooter_logo_open_scooter_page(self, driver):
        driver.maximize_window()
        driver.get(OrderPage.url)

        page = HeaderPage(driver)
        page.click_scooter_logo()

        page = MainPage(driver)

        assert page.url == driver.current_url

    @allure.title('Проверка работы кнопки логотипа «Яндекс»')
    @allure.description('Если нажать на логотип «Яндекс», попадёшь на главную страницу «Яндекс».')
    def test_click_on_yandex_logo_open_yandex_page(self, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = HeaderPage(driver)
        page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[-1])
        yandex = yandex_page.YandexPage(driver)

        assert yandex.url == driver.current_url

