import math 
def square(x):
    s=x**2
    return s
def circle(x):
    s=3.14*x*x
    return s
def equ_tri(x):
    s=math.sqrt(3)*x*x/4
    return s
def choose():
    x,b=-1,-1
    while x<=0:
        x=eval(input("Input a number"))
    while b not in [1,2,3]:
        b=eval(input("Choose a mod:\n1 for square\n2 for circle\n3 for equalilateral triangle:"))
    if b==1:
        s=square(x)
    elif b==2:
        s=circle(x)
    elif b==3:
        s=equ_tri(x)
    print (s)
choose()
