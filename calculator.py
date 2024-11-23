# Complete implementation of all required functions

# Step 1: Add, Subtract, Multiply
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Step 2: Divide
def divide(x, y):
    if y == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return x / y

# Step 3: Square, Power, Square Root
def square(x):
    return x * x

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number!"
    return x ** 0.5
