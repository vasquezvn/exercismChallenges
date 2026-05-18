import pytest

from conditionals import is_criticality_balanced, reactor_efficiency, fail_safe

@pytest.mark.parametrize("temperature, neutrons_emitted, expected", [
    (750, 650, True), (799, 501, True), (500, 600, True),
    (1000, 800, False), (800, 500, False), (800, 500.01, False),
    (799.99, 500, False), (500.01, 999.99, False), (625, 800, False),
    (625.99, 800, False), (625.01, 799.99, False), (799.99, 500.01, True),
    (624.99, 799.99, True), (500, 1000, False), (500.01, 1000, False),
    (499.99, 1000, True)
])
def test_is_criticality_balanced(temperature, neutrons_emitted, expected):
    assert is_criticality_balanced(temperature, neutrons_emitted) == expected

@pytest.mark.parametrize("voltage, current, theoretical_max_power, expected", [
    (10, 1000, 10000, 'green'),
    (10, 999, 10000, 'green'),
    (10, 800, 10000, 'green'),
    (10, 799, 10000, 'orange'),
    (10, 700, 10000, 'orange'),
    (10, 600, 10000, 'orange'),
    (10, 599, 10000, 'red'),
    (10, 560, 10000, 'red'),
    (10, 400, 10000, 'red'),
    (10, 300, 10000, 'red'),
    (10, 299, 10000, 'black'),
    (10, 200, 10000, 'black'),
    (10, 0, 10000, 'black')
])
def test_reactor_efficiency(voltage, current, theoretical_max_power, expected):
    assert reactor_efficiency(voltage, current, theoretical_max_power) == expected

@pytest.mark.parametrize("temperature, neutrons_produced_per_second, threshold, expected", [
    (10, 399, 10000, 'LOW'),
    (10, 300, 10000, 'LOW'), 
    (10, 1, 10000, 'LOW'),
    (10, 0, 10000, 'LOW'), 
    (10, 901, 10000, 'NORMAL'), 
    (10, 1000, 10000, 'NORMAL'),
    (10, 1099, 10000, 'NORMAL'), 
    (10, 899, 10000, 'LOW'), 
    (10, 700, 10000, 'LOW'),
    (10, 400, 10000, 'LOW'), 
    (10, 1101, 10000, 'DANGER'), 
    (10, 1200, 10000, 'DANGER')
])
def test_fail_safe(temperature, neutrons_produced_per_second, threshold, expected):
    assert fail_safe(temperature, neutrons_produced_per_second, threshold) == expected