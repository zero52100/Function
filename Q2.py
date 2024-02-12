"""
Q2.Create a function that takes two arguments, a name and an age, and prints a message like "Hello,   
   [Name]! You are [Age] years old." Call this function with your name and age as arguments. 
"""
try:
    def User(name,age):
        print(f"Hello, {name} ! You are {age} years old.")


    name=(input("Enter your name :"))
    age=int(input("Enter your age :"))

    User(name,age)

except ValueError:
    print("Invalid input !")