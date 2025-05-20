import pytest

from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def bool_func(value: bool) -> bool:
    return value


def test_args_only():
    assert sum_two(1, 9) == 10


def test_kwargs_only():
    assert sum_two(a=1, b=9) == 10


def test_different_args():
    assert sum_two(1, b=9) == 10


@pytest.mark.parametrize("func, args, exc_type", [
    (sum_two, [1, 9.0], TypeError),
    (sum_two, [9.0, 1], TypeError),
    (bool_func, [1], TypeError),
])
def test_invalid_value_type(func, args, exc_type):
    with pytest.raises(exc_type):
        func(*args)
