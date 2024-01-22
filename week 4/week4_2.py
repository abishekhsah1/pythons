"""Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.
"""

def main():
    a=input("enter a string:")
    print("the no of uppercase and lowercase chracter are:",check(a))


c =0
d=0
    
def check(a):
    global c ,d
    
    for char in a:
        if char.isupper():
            c =c+1
        elif char.islower():
            d=d+1
    return c,d
main()
            
