import pytest
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    yield
    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('di@mail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123123')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Раскрываем всплывающее меню
    pytest.driver.find_element_by_xpath('//span[@class="navbar-toggler-icon"]').click()
    # Открываем страницу "Мои питомцы"
    pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()

    # Проверяем, что присутствуют все питомцы
    amount_mypets = pytest.driver.find_element_by_css_selector('.\\.col-sm-4.left').text
    amount_mypets = amount_mypets.split()
    n = amount_mypets.index('Питомцев:') + 1
    mypets_list = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".\\.col-sm-8.right.fill tbody tr"))
    )
    assert len(mypets_list) == int(amount_mypets[n])

    images = pytest.driver.find_elements_by_css_selector('th[scope="row"] img')
    names = pytest.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr/td[1]')
    animal_type = pytest.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr/td[2]')
    age = pytest.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr/td[3]')

    # Проверяем, что хотя бы у половины питомцев есть фото
    count = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') == '':
            count += 1
    assert int(amount_mypets[n]) / 2 >= count

    # Проверяем, что у всех питомцев есть имя, порода и возраст
    for i in range(len(images)):
        assert names[i].text != ''
        assert animal_type[i].text != ''
        assert age[i].text != ''

    # Проверяем, что у всех питомцев разные имена
    all_names = []
    for i in range(len(images)):
        all_names += (names[i].text).split()
    assert len(all_names) == len(set(all_names))

    # Проверяем, что в списке нет повторяющихся питомцев
    all_pets = pytest.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr')
    my_list = []
    for i in range(len(images)):
        pets = all_pets[i].text
        pets = pets.split()
        del pets[-1]
        my_list.append(pets)
    for item1, item2 in itertools.combinations(my_list, 2):
        assert item1 != item2
