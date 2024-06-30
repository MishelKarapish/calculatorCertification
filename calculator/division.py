from calculator.operation import Operation
from calculator.complex_number import ComplexNumber

class Division(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        denominator = b.real**2 + b.imaginary**2
        real = (a.real * b.real + a.imaginary * b.imaginary) / denominator
        imaginary = (a.imaginary * b.real - a.real * b.imaginary) / denominator
        return ComplexNumber(real, imaginary)
