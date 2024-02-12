"""
Q5.Write a Python function that accepts a string and counts the number of upper and lower case letters. 

"""
def count(x):
    lower=0
    upper=0
    for i in x:
      
        if (i>='a'and i<='z'):
            lower=lower+1               
        if (i>='A'and i<='Z'):
            upper=upper+1
    print('Lower case letters: ',lower)
    print('Upper case letters: ',upper)


userinput=(input("Enter the string:"))
count(userinput)