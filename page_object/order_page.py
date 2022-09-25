import allure
from selenium.webdriver.common.by import By


class OrderPage:
    url = 'https://qa-scooter.praktikum-services.ru/order'
    name_field = (By.XPATH, './/input[@placeholder = "* Имя"]')
    last_name_field = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    address_field = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    metro_station_field = (By.XPATH, './/input[@class = "select-search__input"]')
    phone_number_field = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, './/button[text()="Далее"]')
    data_field = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    next_month_button = (By.XPATH, './/button[@aria-label = "Next Month"]')
    rental_period_field = (By.CLASS_NAME, 'Dropdown-arrow')
    comment_field = (By.XPATH, './/input[@placeholder = "Комментарий для курьера"]')
    place_order_button = (
        By.CSS_SELECTOR, '#root > div > div.Order_Content__bmtHS > div.Order_Buttons__1xGrp > button:nth-child(2)')
    yes_button = (By.XPATH, './/button[text()="Да"]')

    def __init__(self, driver):
        self.driver = driver

    # метод проверяет активна ли кнопка «Далее»
    def check_next_button_enabled(self):
        return self.driver.find_element(*self.next_button).is_enabled()

    # метод проверяет активна ли кнопка «Заказать» в форме заказа
    def check_place_order_button_enabled(self):
        return self.driver.find_element(*self.place_order_button).is_enabled()

    # метод проверяет активна ли кнопка «Да» в окне «Хотите оформить заказ?»
    def check_yes_button_enabled(self):
        return self.driver.find_element(*self.yes_button).is_enabled()

    # метод кликает по кнопке «Далее»
    @allure.step('Нажать кнопку «Далее»')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    # метод кликает по кнопке «Да»
    @allure.step('Нажать кнопку «Да» в окне «Хотите оформить заказ?»')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    # метод кликает по кнопке «Заказать» в форме
    @allure.step('Нажать кнопку «Заказать» в форме')
    def click_place_order_button(self):
        self.driver.find_element(*self.place_order_button).click()

    # метод заполняет поле «Имя»
    def set_name(self, name):
        self.driver.find_element(*self.name_field).clear()
        self.driver.find_element(*self.name_field).send_keys(name)

    # метод заполняет поле «Фамилия»
    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).clear()
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    # метод заполняет поле «Адрес»
    def set_address(self, address):
        self.driver.find_element(*self.address_field).clear()
        self.driver.find_element(*self.address_field).send_keys(address)

    # метод заполняет поле «Телефон»
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).clear()
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    # метод заполняет поле «Станция метро»
    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_field).click()
        self.driver.find_element(By.XPATH, f'.//*[text()="{metro_station}"]').click()

    # метод заполения формы «Для кого самокат»: объединяет заполнение всех полей и клик по кнопке «Далее»
    @allure.step('Заполнить все поля в форме «Для кого самокат»')
    def fill_place_order_form1(self, name, last_name, phone_number, metro_station, address):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)

    # метод кликает по кнопке «Следующий месяц» в календаре
    def click_next_month_button(self):
        self.driver.find_element(*self.next_month_button).click()

    @allure.step('Выбрать дату')
    def set_date_in_next_month(self, date):
        self.driver.find_element(*self.data_field).click()
        self.click_next_month_button()
        self.driver.find_element(By.XPATH, f'.//div[text()="{date}"]').click()

    @allure.step('Выбрать количество дней аренды')
    def set_rental_period(self, days):
        period = {
            1: 'сутки',
            2: 'двое суток',
            3: 'трое суток',
            4: 'четверо суток',
            5: 'пятеро суток',
            6: 'шестеро суток',
            7: 'семеро суток'
        }
        self.driver.find_element(*self.rental_period_field).click()
        self.driver.find_element(By.XPATH, f'.//div[text()="{period[days]}"]').click()

    @allure.step('Выбрать цвет самоката')
    def set_color(self, color):
        self.driver.find_element(By.ID, f'{color}').click()

    @allure.step('Указать комментарий к заказу')
    def set_comment(self, text):
        self.driver.find_element(*self.comment_field).clear()
        self.driver.find_element(*self.comment_field).send_keys(text)

    # метод заполения формы «Про аренду»: объединяет заполнение всех полей и клик по кнопке «Заказать»
    # это и есть шаг
    def fill_place_order_form2(self, date=20, days=4, color='black', text='Some test comment'):
        self.set_date_in_next_month(date)
        self.set_rental_period(days)
        self.set_color(color)
        self.set_comment(text)
        # self.check_place_order_button_enabled()
        # self.click_place_order_button()
        # self.check_yes_button_enabled()
        # self.click_yes_button()
