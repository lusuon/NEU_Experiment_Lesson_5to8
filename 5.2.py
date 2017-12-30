a=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
a.sort()
print(a)
small,big=a[0],a[-1]
b=eval(input('Enter a number:'))
if b<a[0] or b>a[-1]:
    print('No such number')
else:
    mid=len(a)//2
    while b!=a[mid]:
        if b<a[mid]:
            if b>a[mid-1]:
                print('No such number')
                break
            big=a[mid]
        else:
            if b<a[mid+1]:
                print('No such number')
                break
            small=a[mid]
        check=mid
        mid=(a.index(big)+a.index(small))//2
        if check == mid:
            if mid<len(a)-2:
                mid+=2
            else:
                mid+=1
    else:
        print ('The index is:',a.index(b))
