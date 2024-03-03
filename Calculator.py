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


# Тести для класу Calculator
import pytest


@pytest.fixture----
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
