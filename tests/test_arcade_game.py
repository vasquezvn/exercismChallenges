import pytest

from arcade_game import eat_ghost, score, lose, win

@pytest.mark.parametrize("power_pellet_active, touching_ghost, expected", [
    (False, True, False),
    (True, False, False),
    (True, True, True)
])
def test_eat_ghost(power_pellet_active, touching_ghost, expected):
    assert eat_ghost(power_pellet_active, touching_ghost) == expected

@pytest.mark.parametrize("touching_power_pellet, touching_dot, expected", [
    (False, False, False),
    (False, True, True),
    (True, False, True)
])
def test_score(touching_power_pellet, touching_dot, expected):
    assert score(touching_power_pellet, touching_dot) == expected

@pytest.mark.parametrize("power_pellet_active, touching_ghost, expected", [
    (True, False, False),
    (True, True, False),
    (False, True, True)
])
def test_lose(power_pellet_active, touching_ghost, expected):
    assert lose(power_pellet_active, touching_ghost) == expected

@pytest.mark.parametrize("has_eaten_all_dots, power_pellet_active, touching_ghost, expected", [
    (True, False, True, False),
    (False, True, True, False),
    (True, True, True, True),
    (True, False, False, True)
])
def test_win(has_eaten_all_dots, power_pellet_active, touching_ghost, expected):
    assert win(has_eaten_all_dots, power_pellet_active, touching_ghost) == expected
    