"""
Q4.Write a Python program to reverse a string """

def rev(x):
    return x[::-1]

userinput=input("Enter a string to be reversed :")
print(f"Input String :- {userinput},\nreversed string {rev(userinput)}")