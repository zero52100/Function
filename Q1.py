"""
Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example. 
"""

def fact(num):
    if(num==0):
        return 1
    return num * fact(num-1)
num=int(input("enter the number "))
print(f"the fatorial of {num} is  {fact(num)} ")


"""
Demonstrate how to call this function with an example. 
 user input num=5
 def fact(5)  <-- value 5 is pased to the function 

 return 5*fact(4)  <-- it will calculate 5 * 4 * 3 * 2 * 1,

"""

