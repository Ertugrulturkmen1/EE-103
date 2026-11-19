def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
   return a / b
def calculator(operation, x, y):
    return operation(x, y)

print(calculator(add, 3, 5), add(3, 5))

