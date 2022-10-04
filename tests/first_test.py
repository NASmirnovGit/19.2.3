import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_miltiply_calculate_corrently(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) ==5