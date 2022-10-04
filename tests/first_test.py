import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_miltiply_calculate_corrently(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) ==5

    def test_division_calculate_corrently(self):
        assert self.calc.division(self, 2, 2) == 4

    def test_division_calculation_failed(self):
        assert self.calc.division(self, 2, 2) == 4

    def test_subtraction_calculate_corrently(self):
        assert self.calc.subtraction(self, 2, 2) == 4

    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 2, 2) == 4

    def test_adding_calculate_corrently(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 2, 2) == 4

