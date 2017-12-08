a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a.sort()
print(a)
b=eval(input("Input a number:"))
mid=len(a)//2
while a!=[mid]:
    if b==a[mid]:
        print(mid)
        break
    if b<a[mid]:
        mid=mid//2
    elif b>a[mid]:
        mid=(len(a)+mid)//2
    if (mid==14 and b!=a[mid]) or (mid==0 and b!=a[mid]):
        print('No such number')
        break
