from calculator.operation import Operation
from calculator.complex_number import ComplexNumber

class Multiplication(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        real = a.real * b.real - a.imaginary * b.imaginary
        imaginary = a.real * b.imaginary + a.imaginary * b.real
        return ComplexNumber(real, imaginary)

