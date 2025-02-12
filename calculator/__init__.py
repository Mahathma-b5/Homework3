'''calculations'''
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """A simple calculator that performs basic arithmetic operations."""
    @staticmethod
    def add(first_operand, second_operand):
        """Returns the sum of two operands."""
        calculation = Calculation(first_operand,second_operand,add)
        return calculation.get_result()
    @staticmethod
    def subtract(first_operand,second_operand):
        """Returns the difference between two operands."""
        calculation = Calculation(first_operand,second_operand,subtract)
        return calculation.get_result()
    @staticmethod
    def multiply (first_operand,second_operand):
        """Returns the product of two operands."""
        calculation = Calculation(first_operand,second_operand, multiply)
        return calculation.get_result()
    @staticmethod
    def divide(first_operand,second_operand):
        """Returns the quotient of two operands."""
        calculation = Calculation(first_operand,second_operand, divide)
        return calculation.get_result()
