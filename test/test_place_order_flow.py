import allure
from selenium import webdriver

from page_object import header
from page_object import order_page


class TestPlaceOrder:
    driver = None
    url = 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка успешного создания заказа по кнопке в хедере')
    @allure.testcase(
        'https://practicum.yandex.ru/learn/qa-automation-web-python/courses/0bee8022-7fad-40dc-b991-efe7d5e2fd81'
        '/sprints/72258/topics/3316c4b2-86cc-48e5-ad4c-027129723286/lessons/023971f0-c1e5-4bc7-8e91-d05260a54fe0/',
        'Тест-кейс')
    # @allure.step('Открыть главную страницу {self.url}')
    def test_place_order_via_header(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        page = header.HeaderPage(self.driver)
        page.check_header_order_button_enabled()
        page.click_header_order_button()
        page.click_cookie_button()

        page = order_page.OrderPage(self.driver)
        page.fill_place_order_form1(
            name='Петр',
            last_name='Петров',
            phone_number='79995554433',
            metro_station='Бульвар Рокоссовского',
            address='Москва, Щелковский проспект, 15, кв. 11')
        page.click_next_button()

        page.fill_place_order_form2(
            date=21,
            color='grey'
        )

        page.check_place_order_button_enabled()
        page.click_place_order_button()
        page.click_yes_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
