Alice={'Chinese':60,'Math':70,'English':80}
Bob={'Chinese':70,'Math':80,'English':90}
Carl={'Chinese':80,'Math':90,'English':100}
Dell={'Chinese':90,'Math':100,'English':60}
Eden={'Chinese':100,'Math':60,'English':70}
Classes=['Chinese','Math','English']
SUM,AVE=0,0
stu=[Alice,Bob,Carl,Dell,Eden]
for i in Classes:
    for j in stu:
        SUM+=j[i]
    AVE=SUM/5
    print(i,':',SUM,'The average:',AVE)
    SUM,AVE=0,0
