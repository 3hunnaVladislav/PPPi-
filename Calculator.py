class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


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
