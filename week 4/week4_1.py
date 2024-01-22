"""Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function"""


def num():
    a =int(input("enter a number:"))
    print("the number in range od 1-200:", check(a))
    
def check(a):
    if a not in range(0,201):
        return False
    else:
        return True
num()
    
   
    