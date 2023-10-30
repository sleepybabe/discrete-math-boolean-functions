f=input("Введите вектор функции\n")
SDNFlist=[]
vectorList=list(f)
if len(f)==4:
    for i in range(len(vectorList)):
        if vectorList[i]=='1':
            if i==0:
                k1="~x&~y"
                SDNFlist.append(k1)
            if i==1:
                k2="~x&y"
                SDNFlist.append(k2)
            if i==2:
                k3="x&~y"
                SDNFlist.append(k3)
            if i==3:
                k4="x&y"
                SDNFlist.append(k4)
elif len(f)==8:
    for i in range(len(vectorList)):
        if vectorList[i]=='1':
            if i==0:
                k1="~x&~y&~z"
                SDNFlist.append(k1)
            if i==1:
                k2="~x&~y&z"
                SDNFlist.append(k2)
            if i==2:
                k3="~x&y&~z"
                SDNFlist.append(k3)
            if i==3:
                k4="~x&y&z"
                SDNFlist.append(k4)
            if i==4:
                k5="x&~y&~z"
                SDNFlist.append(k5)
            if i==5:
                k6="x&~y&z"
                SDNFlist.append(k6)
            if i==6:
                k7="x&y&~z"
                SDNFlist.append(k7)
            if i==7:
                k8="x&y&z"
                SDNFlist.append(k8)
else:
    print("Длина вектора функции введена не верно для 2-х или 3-х переменных")
if len(SDNFlist)==0:
    print("Для введённого вектора функции СДНФ не существует")
else:
    print("СДНФ:")
    print(*SDNFlist, sep='|')

    
