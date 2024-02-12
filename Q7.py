"""
Q7.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items : green-red-yellow-black-white 
Expected Result : black-green-red-white-yellow 
"""
def sort(x):
    words = x.split('-') 
    sortedword = sorted(words) 
    result = '-'.join(sortedword) 
    return result

input= input("Enter a hyphen-separated sequence: ")
output= sort(input)
print("Sorted :", output)
