from calculator.operation import Operation
from calculator.complex_number import ComplexNumber

class Addition(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(a.real + b.real, a.imaginary + b.imaginary)
