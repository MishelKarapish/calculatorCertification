import logging
from calculator.complex_number import ComplexNumber
from calculator.addition import Addition
from calculator.multiplication import Multiplication
from calculator.division import Division

def main():
    logging.basicConfig(level=logging.INFO)

    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(4, 5)

    addition = Addition()
    addition_result = addition.execute(num1, num2)
    print(f"Addition Result: {addition_result}")

    multiplication = Multiplication()
    multiplication_result = multiplication.execute(num1, num2)
    print(f"Multiplication Result: {multiplication_result}")

    division = Division()
    division_result = division.execute(num1, num2)
    print(f"Division Result: {division_result}")

if __name__ == "__main__":
    main()

