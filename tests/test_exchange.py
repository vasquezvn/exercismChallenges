import pytest

from exchange import exchange_money, get_change, get_value_of_bills, get_number_of_bills, get_leftover_of_bills, exchangeable_value

@pytest.mark.parametrize("budget, exchage_rate, expected", [
    (100000, 0.8, 125000),
    (700000, 10.0, 70000)
])
def test_exchange_money(budget, exchage_rate, expected):
    assert exchange_money(budget, exchage_rate) == expected

@pytest.mark.parametrize("budget, exchanging_value, expected", [
    (463000, 5000, 458000),
    (1250, 120, 1130),
    (15000, 1380, 13620)
])
def test_get_change(budget, exchanging_value, expected):
    assert get_change(budget, exchanging_value) == expected

@pytest.mark.parametrize("denomination, number_of_bills, expected", [
    (10000, 128, 1280000),
    (50, 360, 18000),
    (200, 200, 40000)
])
def test_get_value_of_bills(denomination, number_of_bills, expected):
    assert get_value_of_bills(denomination, number_of_bills) == expected

@pytest.mark.parametrize("amount, denomination, expected", [
    (163270, 50000, 3),
    (54361, 1000, 54)
])
def test_get_number_of_bills(amount, denomination, expected):
    assert get_number_of_bills(amount, denomination) == expected

@pytest.mark.parametrize("amount, denomination, expected", [
    (10.1, 10, 0.1),
    (654321.0, 5, 1.0),
    (3.14, 2, 1.14)
])
def test_get_leftover_of_bills(amount, denomination, expected):
    assert get_leftover_of_bills(amount, denomination) == expected

@pytest.mark.parametrize("budget, exchange_rate, spread, denomination, expected", [
    (100000, 10.61, 10, 1, 8568),
    (1500, 0.84, 25, 40, 1400),
    (470000, 1050, 30, 10000000000, 0),
    (470000, 0.00000009, 30, 700, 4017094016600),
    (425.33, 0.0009, 30, 700, 363300)
])
def test_exchangeable_value(budget, exchange_rate, spread, denomination, expected):
    assert exchangeable_value(budget, exchange_rate, spread, denomination) == expected