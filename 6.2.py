def cal():
    a=eval(input('Enter the first number:'))
    b=eval(input('Enter the second number:'))
    a,b=max(a,b),min(a,b)
    print(a,b)
    while (a%b)!=0:
        a=a%b
        a,b=max(a,b),min(a,b)
    print (b)
cal()
