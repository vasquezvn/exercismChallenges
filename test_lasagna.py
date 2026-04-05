import pytest
from lasagna import EXPECTED_BAKE_TIME, bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes

def test_expected_bake_time():
    assert EXPECTED_BAKE_TIME == 40


@pytest.mark.parametrize("num, expected", [
    (1, 39),
    (2, 38),
    (5, 35),
    (10, 30),
    (15, 25),
    (23, 17),
    (33, 7),
    (39, 1)
])
def test_bake_time_remaining(num, expected):
    assert bake_time_remaining(num) == expected

# input_data = [1, 2, 5, 8, 11, 15]
# result_data = [2, 4, 10, 16, 22, 30]

@pytest.mark.parametrize("num, expected", [
    (1, 2), 
    (2, 4),
    (5, 10),
    (8, 16),
    (11, 22),
    (15, 30)
])
def test_preparation_time_in_minutes(num, expected):
    assert preparation_time_in_minutes(num) == expected

# layer_data = (1, 2, 5, 8, 11, 15)
# time_data = (3, 7, 8, 4, 15, 20)
# result_data = [5, 11, 18, 20, 37, 50]

@pytest.mark.parametrize("layer, time, expected", [
    (1, 3, 5),
    (2, 7, 11),
    (5, 8, 18),
    (8, 4, 20),
    (11, 15, 37),
    (15, 20, 50)
])
def test_elapsed_time_in_minutes(layer, time, expected):
    assert elapsed_time_in_minutes(layer, time) == expected

@pytest.mark.parametrize("function", [
    (bake_time_remaining),
    (preparation_time_in_minutes),
    (elapsed_time_in_minutes)
])
def test_docstrings_were_written(function: function):
    actual_result = function.__doc__
    print(f'Called {function.__name__}.__doc__, {actual_result} was returned.')

    assert len(actual_result) != 0