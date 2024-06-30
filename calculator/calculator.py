from .complex_number import ComplexNumber
from .operation import Operation

class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        logger.info(f"Calculating: {a} and {b}")
        result = self.operation.execute(a, b)
        logger.info(f"Result: {result}")
        return result