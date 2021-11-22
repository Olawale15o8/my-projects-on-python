import math
def quadratic():
    a=int(input("enter the co_efficient of x_square : "))
    b=int(input("enter the co_efficient of x  : "))
    c=int(input("enter the constant number given  :  "))
    q = b*b
    d= 4*a*c
    x = math.sqrt(q-d)
    r = (-b+x)/(2*a)
    s = (-b-x)/(2*a)
    print(f"x= {r}  or  {s}")
quadratic()  
