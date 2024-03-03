class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Ділення на нуль неможливе")
        return x / y


    def power(self, x, n):
        return x ** n  # Розрахунок степені числа

    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y
        return x  # Найбільший спільний дільник



# Тести для класу Calculator
import pytest



@pytest.fixture

def calculator():
    return Calculator()


class TestCalculator:
    def test_add(self, calculator):
        # Arrange
        x = 5
        y = 3
        # Act
        result = calculator.add(x, y)
        # Assert
        assert result == 8, "Додавання цілих чисел повинно повертати їх суму"

    def test_subtract(self, calculator):
        # Arrange
        x = 5
        y = 3
        # Act
        result = calculator.subtract(x, y)
        # Assert
        assert result == 2, "Віднімання цілих чисел повинно повертати їх різницю"

    def test_multiply(self, calculator):
        # Arrange
        x = 5
        y = 3
        # Act
        result = calculator.multiply(x, y)
        # Assert
        assert result == 15, "Множення цілих чисел повинно повертати їх добуток"

    def test_divide(self, calculator):
        # Arrange
        x = 10
        y = 2
        # Act
        result = calculator.divide(x, y)
        # Assert
        assert result == 5, "Ділення цілих чисел повинно повертати їх частку"


    def test_power(self, calculator):
        # Arrange
        x = 2
        n = 3
        # Act
        result = calculator.power(x, n)
        # Assert
        assert result == 8, "Піднесення числа до степені повинно повертати правильний результат"

<<<<<<< HEAD
=======
    def test_gcd(self, calculator):
        # Arrange
        x = 24
        y = 36
        # Act
        result = calculator.gcd(x, y)
        # Assert
        assert result == 12, "НСД чисел 24 та 36 повинен бути 12"
>>>>>>> ecacb68 (Add gcd operation)
