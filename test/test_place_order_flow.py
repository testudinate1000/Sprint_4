import allure

from page_object.header import HeaderPage
from page_object.order_page import OrderPage
from page_object.main_page import MainPage


class TestPlaceOrder:
    driver = None
    url = MainPage.url

    @allure.title('Проверка успешного создания заказа по кнопке в хедере')
    def test_place_order_via_header(self, driver, user_data):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()

        page = HeaderPage(driver)
        page.check_header_order_button_enabled()
        page.click_header_order_button()

        page = OrderPage(driver)
        page.fill_place_order_form1(
            name=user_data[0],
            last_name=user_data[1],
            phone_number=user_data[2],
            metro_station=user_data[3],
            address=user_data[4]
        )
        page.click_next_button()
        page.fill_place_order_form2(date=21, color='grey')
        page.check_place_order_button_enabled()
        page.click_place_order_button()
        page.click_yes_button()

    @allure.title('Проверка успешного создания заказа по кнопке на главной странице')
    def test_place_order_via_main_page(self, driver, user_data):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.place_order_button)
        page.click_place_order_button()

        page = OrderPage(driver)
        page.fill_place_order_form1(
            name=user_data[0],
            last_name=user_data[1],
            phone_number=user_data[2],
            metro_station=user_data[3],
            address=user_data[4]
        )
        page.click_next_button()
        page.fill_place_order_form2(date=21, color='grey')
        page.check_place_order_button_enabled()
        page.click_place_order_button()
        page.click_yes_button()
