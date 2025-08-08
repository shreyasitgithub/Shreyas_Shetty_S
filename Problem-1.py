class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def operate(self, operation: str):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()
    calc = Calculator(a, b)
    print("Result:", calc.operate(op))
