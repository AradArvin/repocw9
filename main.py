from math_operations.addition import addit
from math_operations.subtraction import subit
from math_operations.multiplication import miltit
from math_operations.division import divit


if __name__=="__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(addit(a,b))
    print("addition:",addit(a,b))
    print("subtraction:",subit(a,b))
    print("multiplication:",miltit(a,b))
    print("division:",divit(a,b))
    

