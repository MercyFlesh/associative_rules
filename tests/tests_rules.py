import sys
import copy
sys.path.append('../associative_rules')
import apriori
import rules
import pytest
import allure

apriori_result = {('007',): 0.8, ('Yandex',): 0.9, ('007', 'Yandex'): 0.8}
confidience_result = {(('007',), ('Yandex',)): [0.8, 0.9, 0.8, 1.0], (('Yandex',), ('007',)): [0.9, 0.8, 0.8, 0.8889]}


@allure.step('Checking _get_keys_combinations function')
def test_get_keys_combinations():
    expected_result = [[('007',)], [('Yandex',)], [('007', 'Yandex')], [('007',), ('Yandex',)], [('007',), ('007', 'Yandex')], [('007', 'Yandex'), ('Yandex',)]]
    actual_result = list(rules._get_keys_combinations(apriori_result))
    assert expected_result == actual_result

@allure.step('Checking _confidience function')
def test_confidience():
    expected_result = copy.deepcopy(confidience_result)
    actual_result = dict()
    rules._confidience(actual_result, apriori_result, 0)
    assert expected_result.items() <= actual_result.items()

@allure.step('Checking _lift function')
def test_lift():
    expected_result = {(('007',), ('Yandex',)): [0.8, 0.9, 0.8, 1.0, 1.1111], (('Yandex',), ('007',)): [0.9, 0.8, 0.8, 0.8889, 1.1111]}
    actual_result = copy.deepcopy(confidience_result)
    rules._lift(actual_result, 0.1)
    assert expected_result.items() <= actual_result.items()

@allure.step
def test_levarage():
    expected_result = {(('007',), ('Yandex',)): [0.8, 0.9, 0.8, 1.0, 0.08], (('Yandex',), ('007',)): [0.9, 0.8, 0.8, 0.8889, 0.08]}
    actual_result = copy.deepcopy(confidience_result)
    rules._levarage(actual_result, 0)
    assert expected_result.items() <= actual_result.items()

@allure.step('Checking _conviction function')
def test_conviction():
    expected_result = {(('007',), ('Yandex',)): [0.8, 0.9, 0.8, 1.0, 'inf'], (('Yandex',), ('007',)): [0.9, 0.8, 0.8, 0.8889, 1.8002]}
    actual_result = copy.deepcopy(confidience_result)
    rules._conviction(actual_result, 0)
    assert expected_result.items() <= actual_result.items()

@allure.step('Checking get_associative_rules function')
def test_get_associative_rules():
    expected_result = {(('007',), ('Yandex',)): [0.8, 0.9, 0.8, 1.0, 1.1111, 0.08, 'inf'], (('Yandex',), ('007',)): [0.9, 0.8, 0.8, 0.8889, 1.1111, 0.08, 1.8002]}
    actual_result = rules.get_associative_rules(apriori_result, 0, 0, 0, 0)
    assert expected_result == actual_result
