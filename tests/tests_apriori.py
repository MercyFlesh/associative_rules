import sys
sys.path.append('../assotiative_rules')
import apriori
import pytest
import allure

data_path = 'username.csv'

@allure.title('Проверка функции чтения csv-файла')
def test_csv_read():
    expected_result = ['Username; Identifier;First name;Last name']
    data = apriori._csv_read(data_path)
    actual_result = next(data)
    assert expected_result == actual_result

@allure.title('Проверка работы функции подсчета поддержки')
def test_support():
    expected_result = {(('Username; Identifier;First name;Last name',), 0.2),
        (('grey07;2070;Laura;Grey',), 0.2),
        (('booker12;9012;Rachel;Booker',), 0.2),
        (('jenkins46;9346;Mary;Jenkins',), 0.2),
        (('johnson81;4081;Craig;Johnson',), 0.2)}
    actual_result = apriori._support(apriori._csv_read(data_path), 0.2)
    assert expected_result == actual_result

@allure.title('Проверка работы функции нахождения возможных наборов')
def test_get_L_items():
    expected_result = {('booker12;9012;Rachel;Booker', 'johnson81;4081;Craig;Johnson'),
        ('jenkins46;9346;Mary;Jenkins', 'johnson81;4081;Craig;Johnson'),
        ('Username; Identifier;First name;Last name', 'johnson81;4081;Craig;Johnson'),
        ('Username; Identifier;First name;Last name', 'jenkins46;9346;Mary;Jenkins'),
        ('grey07;2070;Laura;Grey', 'johnson81;4081;Craig;Johnson'),
        ('booker12;9012;Rachel;Booker', 'grey07;2070;Laura;Grey'),
        ('Username; Identifier;First name;Last name', 'grey07;2070;Laura;Grey'),
        ('booker12;9012;Rachel;Booker', 'jenkins46;9346;Mary;Jenkins'),
        ('Username; Identifier;First name;Last name', 'booker12;9012;Rachel;Booker'),
        ('grey07;2070;Laura;Grey', 'jenkins46;9346;Mary;Jenkins')}
    actual_result = apriori._get_L_items(list((dict(apriori._support(apriori._csv_read(data_path), 0.2))).keys()), 2)
    assert expected_result == actual_result

@allure.title('Проверка реализации алгоритма apriori')
def test_apriori():
    expected_result = {('johnson81;4081;Craig;Johnson',): 0.2,
        ('Username; Identifier;First name;Last name',): 0.2,
        ('grey07;2070;Laura;Grey',): 0.2,
        ('booker12;9012;Rachel;Booker',): 0.2,
        ('jenkins46;9346;Mary;Jenkins',): 0.2}
    actual_result = apriori.apriori(data_path, 0.2)
    assert expected_result.items() <= actual_result.items()
