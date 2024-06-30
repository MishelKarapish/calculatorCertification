from abc import ABC, abstractmethod
from calculator.complex_number import ComplexNumber

class Operation(ABC):
    @abstractmethod
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        pass

