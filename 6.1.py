a=input("Input some numbers,use space to seperate:")
def AVE(a):
    SUM=0
    for i in list(a.split(' ')):
        SUM+=eval(i)
    ave = SUM/len(list(a.split(' ')))
    return ave
def BIG(ave):
    count=0
    ave=AVE(a)
    for i in list(a.split(' ')):
        if eval(i)>ave:
            count+=1
    return count
def OUT():
    ave=AVE(a)
    count=BIG(ave)
    print('average:',ave,'bigger than average:',count)
    return
OUT()
