# test_calc.py
import pytest
from calculator import Calculator

def test_add_basic():
    """Проверка обычного сложения"""
    calc = Calculator()
    result = calc.add(2, 5)
    assert result == 7, "2 + 5 должно быть равно 7"

def test_divide_basic():
    """Проверка обычного деления"""
    calc = Calculator()
    assert calc.divide(16, 4) == 4


def test_divide_by_zero():
    """
    Негативный тест: Деление на ноль.
    Мы ожидаем, что код ВЫБРОСИТ ошибку ValueError.
    """
    calc = Calculator()
    
    with pytest.raises(ValueError):
        calc.divide(10, 0)


@pytest.mark.parametrize("number, expected", [
    (1, False),  # 1 не простое число
    (2, True),   # 2 простое
    (3, True),   # 3 простое
    (4, False),  # 4 делится на 2
    (5, True),   # 5 простое
    (9, False),  # 9 делится на 3
    (11, True),  # 11 простое
    (-5, False)  # Отрицательные не простые
])
def test_is_prime_number(number, expected):
    """
    Параметризованный тест для проверки простых чисел.
    Этот тест запустится 8 раз (для каждой строчки данных выше).
    """
    calc = Calculator()
    result = calc.is_prime_number(number)
    
    assert result == expected, f"Ошибка проверки числа {number}"

@pytest.mark.parametrize("a, b, expected_sum", [
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 50, 150)
])
def test_add_parametrized(a, b, expected_sum):
    calc = Calculator()
    assert calc.add(a, b) == expected_sum