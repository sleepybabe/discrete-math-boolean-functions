#Метод Квайна - Мак-Класки
import math
import sys

print("Введите количество переменных функции: ")
n=input()
print("Введите вектор функции: ")
s=input()
if not n.isdigit():
    print("Неправильно введено количество переменных!")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()
else:
    n=int(n)

if math.log2(len(s))!=n:
    print("Неправильно введен вектор!")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()

v=[]
vk=0
vvk=0
for i in s:
    if i=='0':
        vk=vk+1
    if i=='1':
        vvk=vvk+1
    if ((i!="0") & (i!="1")):
        print("Неправильно введен вектор!")
        input("Нажмите клавишу Enter, чтобы продолжить...")
        sys.exit()
    v.append(i)
if vk==len(v):
    print("ДНФ не существует!")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()

if vvk==len(v):
    print("Минимальная ДНФ: 1")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()

nabors=[]
for i in range(2**n):
    nabors.append([0] * n)

#print(nabors)

ii=0

for i in range(len(nabors)):
    ii=i
    for j in range(len(nabors[i])-1,-1,-1):
        if ii%2==0:
            nabors[i][j]="0"
        else:
            nabors[i][j]="1"
        ii=int(ii/2)

ednabors=[]
for i in range(2**n):
    if v[i]=='1':
        ednabors.append(nabors[i])

#print(ednabors)
s=''
skleyki=[]
for i in range(len(ednabors)):  #преобразовываем каждый набор в одну строку
    for j in range(len(ednabors[i])):
        s=s+ednabors[i][j]
    skleyki.append(s)
    s=''
# groups=[]
#
# for i in range(n+1):
#     groups.append([])
#     for j in range(len(ednabors)):
#         groupshelp = 0
#         for k in ednabors[j]:
#             if k=='1':
#                 groupshelp=groupshelp+1
#         if groupshelp==i:
#             groups[i].append(ednabors[j])
# groups = [x for x in groups if x]
# print(groups)
# skleyki=[]
# ii=0
# s=''
# help=0

# for i in range(len(groups)-1):
#     ii=i+1
#     for j in range(len(groups[i])):
#         for m in range(len(groups[ii])):
#             for k in range(n):
#                 if (groups[i][j][k]!=groups[ii][m][k]):
#                     s=s+'*'
#                     help=help+1
#                 else:
#                     s=s+groups[i][j][k]
#             print(groups[ii][m])
#             if help>1:
#                 help=0
#                 s = ''
#                 if ii==len(groups):
#                     for t in groups[ii][m]:
#                         s = s + t
#                 else:
#                     for t in groups[i][j]:
#                         s=s+t
#                 skleyki.append(s)
#                 s = ''
#                 continue
#             skleyki.append(s)
#             s=''
#             help = 0

# print(skleyki)

def funcskley(skleykii,rep):  #склеивание
    rep=rep+1
    s = ''
    help=0
    resskleyki = []
    taken = []
    alreadyskl = 0
    added = 0
    for i in range(len(skleykii)):
        ii=i+1
        for j in range(ii, len(skleykii)):
            for k in range(len(skleykii[i])):  #склеивание наборов, используя символ * на месте ОДНОГО символа, если наборы отличаются там
                if (skleykii[i][k]!=skleykii[j][k]):
                    s=s+'*'
                    help=help+1   #проверяет на соседство наборов
                else:
                    s=s+skleykii[i][k]

            if help==1:  #если наборы соседние
                added=1  #пометка, что набор добавлен
                taken.append(skleykii[j])  #добавляет в массив проверки, т.е. склеялся ли уже набор (по j, т.е. мы можем по нему пройтись по i)->
                resskleyki.append(s)       #-> и поэтому мы можем добавить его (что нельзя), если дальше не будет соседних с ним наборов
            s=''
            help=0
        if skleykii[i] in taken: #был ли уже этот набор склеен
            alreadyskl = 1
        if added==0:   #проверяем, что набор не был склеен с последующими наборами
            if alreadyskl<1: #проверяем, что набор не был склеен с предыдущими (!) наборами
                resskleyki.append(skleykii[i])
        alreadyskl=0
        added=0

    if rep!=n:
        resskleyki=set(resskleyki)
        resskleyki=list(resskleyki)
        return funcskley(resskleyki,rep)
    else:
        return resskleyki

#print(skleyki)
resskleyki=funcskley(skleyki,0)
# print(resskleyki)

skleykimatrix=[]
count=0

for i in range(len(resskleyki)):  #сравнение склеек с единичными наборами
    skleykimatrix.append([])
    for j in range(len(ednabors)):
        for k in range(n):
            if ((resskleyki[i][k]==ednabors[j][k]) | (resskleyki[i][k]=='*')):
                count=count+1
        if count==n:
            skleykimatrix[i].append(1)
        else:
            skleykimatrix[i].append(0)
        count=0

#print(skleykimatrix)
help=[]

for i in range(len(ednabors)):  #сравниваем столбцы склейматрицы и если число в столбце равняется 1->
    help.append([])  #-> то добавляем в массив индекс строки этого элемента, т.е. на выходе получим массив->
    for j in range(len(skleykimatrix)):  #где числа будут являться индексами в массиве склеек
        if skleykimatrix[j][i]==1:
            help[i].append(j)
#print(help)

min=[]
currentindexes=[]
allindexes=[]
count=0
countmas=[]
alone=0
for i in range(len(help)):    #выбираем из склеек те, которые наибольше покрывают все наборы
    for j in range(len(help[i])):
        if help[i][j] in allindexes:  #проверяли ли мы уже этот индекс
            count = 0
            countmas = []
            break
        for k in range(i+1,len(help)): #проверяем на частоту встречи определенного индекса (т.е. максимальное число вхождений)
            if help[i][j] in help[k]:  #если индекс находится в последующем наборе индексов
                count=count+1
                if len(help[k]) == 1:  #если набор следующих индексов состоит из одного числа->
                    allindexes.append(help[i][j]) #->то добавляем его в массив результатных индексов
                    alone = 1
                    count = 0
                    countmas = []
                    break
        if alone==0: #если же набор индексов не состоял из одного числа, то добавляем число вхождений этого индекса в массив счета
            countmas.append(count)
            count=0
        else:
            break
    if (len(countmas)!=0) &(alone==0):
        mx = max(countmas)
        ind = countmas.index(mx)  #определяем индекс этого максимума, т.е. индекс максимального индекса
        allindexes.append(help[i][ind])  #добавляем этот индекс в массив результата
    alone=0
    count = 0
    countmas = []

for i in allindexes:  #сверяем полученные индексы со склейками
    min.append(resskleyki[i])
# print(ednabors)
# print(allindexes)
#print(min)

x=''
k=1
minDNF=''
for i in min:
    for j in i:
        if j=='0':
            x=x+'-x'+str(k)
        if j=='1':
            x=x+'x'+str(k)
        k = k + 1
    if i==min[len(min)-1]:
        minDNF=minDNF+x
    else:
        minDNF=minDNF+x+' v '
    k=1
    x=''

print('Минимальная ДНФ:')
print(minDNF)
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()

#10101111
#0101010100000011

#1111001111010001
#1100010100110011
#1100011111111111
#1110

#01101001
#01111111