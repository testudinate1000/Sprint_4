import json
import allure
from pytest import fixture
from selenium import webdriver

data_path = 'user_data.json'


def load_test_data(path):
    with open(path, encoding='utf-8') as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def user_data(request):
    data = request.param
    return data


@allure.step(f'Открыть браузер')
@fixture(params=[webdriver.Chrome
                 # ,
                 # webdriver.Firefox,
                 # webdriver.Edge
                 ])
def driver(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()
