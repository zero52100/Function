"""
Q8.Define a function that accepts 2 values and 
return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type. 
"""

#Function with Argument and Return Type
def operations_with_return(num1, num2):
    sum = num1 + num2
    sub= num1 - num2
    mult= num1 * num2
    return sum, sub, mult

# Function with Argument without Return Type
def operations_without_return(a, b):
    print("Function with Argument without Return Type : -")
    print(f"Sum: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

# Function without Argument with Return Type
def operations_without_argument_with_return():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    sum_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    return sum_result, subtraction_result, multiplication_result

# Function without Argument and without Return Type
def operations_without_argument_without_return():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    print(f"Sum: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

# Argument with Return Type
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
result = operations_with_return(input1, input2)
print("Argument with Return Type : -")
print("Function 1 Results:", result)
# Argument without Return Type
operations_without_return(10, 9)
print("Without Argument with Return Type : -")
# Without Argument with Return Type
result3 = operations_without_argument_with_return()
print("Function 3 Results:", result3)
print("Without Argument without Return Type : -")
# Without Argument without Return Type
operations_without_argument_without_return()
