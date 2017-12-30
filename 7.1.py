import csv,re
a=input('Enter the family name you want to search:')
count=0
with open('customer.txt','r') as nameFile:
    lines=csv.reader(nameFile)
    for i in lines:
        if a.lower() == re.split("[| |'|]",str(i))[-2].lower():
            count+=1
            print(str(i))
    nameFile.close()
print(count)
