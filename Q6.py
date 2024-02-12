"""
Q6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 
"""
def is_prime(num):
    if num < 2:  
        return False
    for i in range(2, num):
        if num % i == 0:
            return False  
    return True  


num=int(input("enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

        
    