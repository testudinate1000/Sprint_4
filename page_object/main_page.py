import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    url = 'https://qa-scooter.praktikum-services.ru/'
    cookie_button = (By.ID, 'rcc-confirm-button')
    place_order_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button')
    FQA_block = (By.XPATH, './/div[@class="Home_SubHeader__zwi_E"]')
    question_1 = (By.CSS_SELECTOR, '#accordion__heading-0')
    question_2 = (By.CSS_SELECTOR, '#accordion__heading-1')
    question_3 = (By.CSS_SELECTOR, '#accordion__heading-2')
    question_4 = (By.CSS_SELECTOR, '#accordion__heading-3')
    question_5 = (By.CSS_SELECTOR, '#accordion__heading-4')
    question_6 = (By.CSS_SELECTOR, '#accordion__heading-5')
    question_7 = (By.CSS_SELECTOR, '#accordion__heading-6')
    question_8 = (By.CSS_SELECTOR, '#accordion__heading-7')
    answer_1 = (By.XPATH, './/div[@id="accordion__panel-0"]/p')
    answer_2 = (By.XPATH, './/div[@id="accordion__panel-1"]/p')
    answer_3 = (By.XPATH, './/div[@id="accordion__panel-2"]/p')
    answer_4 = (By.XPATH, './/div[@id="accordion__panel-3"]/p')
    answer_5 = (By.XPATH, './/div[@id="accordion__panel-4"]/p')
    answer_6 = (By.XPATH, './/div[@id="accordion__panel-5"]/p')
    answer_7 = (By.XPATH, './/div[@id="accordion__panel-6"]/p')
    answer_8 = (By.XPATH, './/div[@id="accordion__panel-7"]/p')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(element))

    # Метод кликает по кнопке «да все привыкли»
    @allure.step('Принять cookie')
    def click_cookie_button(self):
        self.wait_for_element(self.cookie_button)
        self.driver.find_element(*self.cookie_button).click()

    # Метод скроллит страницу до нужного элемента
    @allure.step('Проскроллить страницу')
    def scroll_to_element(self, element):
        self.wait_for_element(element)
        el = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    # метод кликает по кнопке «Заказать» на главной странице
    @allure.step('Нажать кнопку «Заказать»')
    def click_place_order_button(self):
        self.driver.find_element(*self.place_order_button).click()

    @allure.step('Кликнуть на вопрос «Сколько это стоит? И как оплатить?»')
    def click_1_question_button(self):
        element = self.driver.find_element(*self.question_1)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Хочу сразу несколько самокатов! Так можно?»')
    def click_2_question_button(self):
        element = self.driver.find_element(*self.question_2)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Как рассчитывается время аренды?»')
    def click_3_question_button(self):
        element = self.driver.find_element(*self.question_3)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Можно ли заказать самокат прямо на сегодня?»')
    def click_4_question_button(self):
        element = self.driver.find_element(*self.question_4)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Можно ли продлить заказ или вернуть самокат раньше?»')
    def click_5_question_button(self):
        element = self.driver.find_element(*self.question_5)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Вы привозите зарядку вместе с самокатом?»')
    def click_6_question_button(self):
        element = self.driver.find_element(*self.question_6)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Можно ли отменить заказ?»')
    def click_7_question_button(self):
        element = self.driver.find_element(*self.question_7)
        element.click()
        return element

    @allure.step('Кликнуть на вопрос «Я жизу за МКАДом, привезёте?»')
    def click_8_question_button(self):
        element = self.driver.find_element(*self.question_8)
        element.click()
        return element

    def check_1_answer(self):
        answer = self.answer_1
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_2_answer(self):
        answer = self.answer_2
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_3_answer(self):
        answer = self.answer_3
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_4_answer(self):
        answer = self.answer_4
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_5_answer(self):
        answer = self.answer_5
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_6_answer(self):
        answer = self.answer_6
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_7_answer(self):
        answer = self.answer_7
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text

    def check_8_answer(self):
        answer = self.answer_8
        self.wait_for_element(answer)
        element = self.driver.find_element(*answer)
        return element.text
