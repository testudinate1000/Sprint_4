import allure
from pytest import mark

from page_object.main_page import MainPage


@allure.title('Проверка вопросов и ответов в блоке FQA')
class TestFQA:
    driver = None
    url = MainPage.url

    @mark.parametrize('question, answer', [
        ('Сколько это стоит? И как оплатить?',
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')])
    def test_check_1_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_1_question_button()

        assert question == button.text
        assert answer == page.check_1_answer()

    @mark.parametrize('question, answer', [
        ('Хочу сразу несколько самокатов! Так можно?',
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
         'несколько заказов — один за другим.')])
    def test_check_2_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_2_question_button()

        assert question == button.text
        assert answer == page.check_2_answer()

    @mark.parametrize('question, answer', [
        ('Как рассчитывается время аренды?',
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
         'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
         'суточная аренда закончится 9 мая в 20:30.')])
    def test_check_3_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_3_question_button()

        assert question == button.text
        assert answer == page.check_3_answer()

    @mark.parametrize('question, answer', [
        ('Можно ли заказать самокат прямо на сегодня?',
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')])
    def test_check_4_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_4_question_button()

        assert question == button.text
        assert answer == page.check_4_answer()

    @mark.parametrize('question, answer', [
        ('Можно ли продлить заказ или вернуть самокат раньше?',
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')])
    def test_check_5_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_5_question_button()

        assert question == button.text
        assert answer == page.check_5_answer()

    @mark.parametrize('question, answer', [
        ('Вы привозите зарядку вместе с самокатом?',
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
         'передышек и во сне. Зарядка не понадобится.')])
    def test_check_6_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_6_question_button()

        assert question == button.text
        assert answer == page.check_6_answer()

    @mark.parametrize('question, answer', [
        ('Можно ли отменить заказ?',
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')])
    def test_check_7_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_7_question_button()

        assert question == button.text
        assert answer == page.check_7_answer()

    @mark.parametrize('question, answer', [
        ('Я живу за МКАДом, привезёте?',
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.')])
    def test_check_8_answer_shown(self, question, answer, driver):
        driver.maximize_window()
        driver.get(self.url)

        page = MainPage(driver)
        page.click_cookie_button()
        page.scroll_to_element(MainPage.FQA_block)
        button = page.click_8_question_button()

        assert question == button.text
        assert answer == page.check_8_answer()
