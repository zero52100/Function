"""
Q3.Write a Python function to find the maximum of three numbers. 
"""
def maxnum(num1,num2,num3):
    
    print(f"The maximum of three numbers is {max(num1,num2,num3)}")


num1=int(input("Enter First number :"))
num3=int(input("Enter Second number :"))
num2=int(input("Enter Third number :"))

maxnum(num1,num2,num3)