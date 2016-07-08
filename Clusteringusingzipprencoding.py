from _ast import Name

import xlrd
from xlwt import Workbook
import operator
path = "G:/VMC_spread_data_500.csv"
book = xlrd.open_workbook(path)

limit =499#number of zipprs
k=20
k1=0.9
k2=0.1

first_sheet = book.sheet_by_index(0)
zipprs=first_sheet.col_values(0)
zipprs=zipprs[0:limit]
del zipprs[0]
Y=first_sheet.col_values(1)
Y=Y[0:limit]
del Y[0]
X=first_sheet.col_values(2)
X=X[0:limit]
del X[0]
clstrwith2 = first_sheet.col_values(3)
clstrwith2=clstrwith2[0:limit]
del clstrwith2[0]
clstrwith3 = first_sheet.col_values(4)
clstrwith3=clstrwith3[0:limit]
del clstrwith3[0]
clstrwith4 = first_sheet.col_values(5)
clstrwith4=clstrwith4[0:limit]
del clstrwith4[0]

c2=0
c3=0
c4=0
dict4={}
dict2={}
dict3={}
for i in range(len(clstrwith2)):
    dict2[str(clstrwith2[i])]=0
for i in range(len(clstrwith3)):
    dict3[str(clstrwith3[i])]=0
for i in range(len(clstrwith4)):
    dict4[str(clstrwith4[i])]=0

for i in range(len(clstrwith2)):
    dict2[str(clstrwith2[i])]+=1
for i in range(len(clstrwith3)):
    dict3[str(clstrwith3[i])]+=1
for i in range(len(clstrwith4)):
    dict4[str(clstrwith4[i])]+=1

#ok till here :P

def zipprvalue(a):
    if(a[2].isalpha()):
        a2=ord(a[2])-55
    else:
        a2=int(a[2])
    if(a[3].isalpha()):
        a3=ord(a[3])-55
    else:
        a3=int(a[3])
    return a2*36+a3
#for distance between zipprs => GIVE TWO NAMES OF ROADS
def zipprdistance(a,b):
    if a[1]!=b[1]:
        return 10000000
    else:
        if(a[2].isalpha()):
            a2=ord(a[2])-55
        else:
            a2=int(a[2])

        if(a[3].isalpha()):
            a3=ord(a[3])-55
        else:
            a3=int(a[3])
        if(b[3].isalpha()):
            b3=ord(b[3])-55
        else:
            b3=int(b[3])
        if(b[2].isalpha()):
            b2=ord(b[2])-55
        else:
            b2=int(b[2])
        return 36*(abs(a2-b2))+abs(a3-b3)
def CostfunctionMatrix(ValueList,NameList,dict4):
    dist=[]
    for i in range(len(ValueList)):
        list2=[]
        for j in range(len(ValueList)):
            if i==j:
                list2.append(1000000000)
            else:
                list2.append( (k1*(dict4[NameList[i]]+dict4[NameList[j]]))/limit + (k2*zipprdistance(NameList[i],NameList[j]))/MaxDistance )
        dist.append(list2)
    return dist

#doubt about this method
def generateDistbetweenzipprs(NameList):
    dist=[]
    for i in range(len(NameList)):
        list2=[]
        for j in range(len(NameList)):
            if i==j:
                list2.append(-1)
            else:
                if(zipprdistance(NameList[i],NameList[j])==10000000):
                    list2.append(-1)
                else:
                    list2.append(zipprdistance(NameList[i],NameList[j]))
        dist.append(list2)
    return dist

def getMin(dist):
    n=len(dist)
    m=len(dist[0])
    Min=1<<30
    Ii=-1
    Ji=-1
    for i in range(n):
        for j in range(m):
            if(dist[i][j]<Min and dist[i][j]!=-1):
                Ii=i
                Ji=j
                Min=dist[i][j]
    return (Ii,Ji)

c4=len(dict4)
print c4


NameList = []
ValueList=[]
answerDict = {}   #Specifies the subclusters in a big cluster
for i in dict4:
    NameList.append(i)
NameList.sort()
print NameList
for i in range(len(NameList)):
    ValueList.append(zipprvalue(NameList[i]))

DupNameList = NameList
DupDict4 = dict4

CentroidList=ValueList
RadiusList=[]

for i in range(len(ValueList)):
    RadiusList.append(0)

#initialising answerDict
for i in range(len(NameList)):
    tem_list = []
    tem_list.append(NameList[i])
    answerDict[NameList[i]] = tem_list

ooo=generateDistbetweenzipprs(NameList)
MaxDistance=-1
for i in range(len(ooo)):
    for j in range(len(ooo[0])):
        MaxDistance=max(MaxDistance,ooo[i][j])
print MaxDistance


# print answerDict
dist = CostfunctionMatrix(ValueList,NameList,dict4)


for oo in range(c4 - k):
    x, y = getMin(dist)
    if NameList[x] == "Spam" or NameList[y] == "Spam":
        continue
    xx = CentroidList[x]
    yy = CentroidList[y]
    pp=int(dict4[NameList[x]]*CentroidList[x]+dict4[NameList[y]]*CentroidList[y])
    lol=int(dict4[NameList[x]]*1+dict4[NameList[y]])
    CentroidList[x] = pp/lol
    RadiusList[x]=int(dict4[NameList[x]]*abs(CentroidList[x]-xx)+dict4[NameList[y]]*abs(yy-CentroidList[x]))/int(dict4[NameList[x]]+dict4[NameList[y]])
    CentroidList[y]=-1
    RadiusList[y]=10000000000
    dict4[NameList[x]] += dict4[NameList[y]]
    del dict4[NameList[y]]
    answerDict[NameList[x]].extend(answerDict[NameList[y]])
    del answerDict[NameList[y]]
    NameList[y]="Spam"
    ValueList[y]=-1
    for i in range(len(NameList)):
        dist[i][y] = 10000000000
        dist[y][i] = 10000000000
    for i in range(len(NameList)):
        if(dist[i][x]!=10000000000 and dist[x][i]!=10000000000 and i!=x):
            dist[i][x]=(k1*(dict4[NameList[i]]+dict4[NameList[x]]))/limit +(k2*(zipprdistance(NameList[i],NameList[x])))/MaxDistance
            dist[x][i]=dist[i][x]

#Clusterlist  =>  gives the list of clusters finally achieved
Clusterlist = answerDict.keys()
Clusterlist.sort()
print Clusterlist

Final_Answer = sorted(answerDict.items(),
                      key=operator.itemgetter(1))  # Final_Answer is a list storing the clusters.
#Final_Answer is sorted form of Clusterlist
for r in Final_Answer:
    print r

Answer_dict = {}
for i in range(len(DupNameList)):
    Answer_dict[DupNameList[i]] = 0
for i in range(k):
    templist = []
    templist = Final_Answer[i][1]
    for j in range(len(templist)):
        Answer_dict[templist[j]] = i + 1

asdf = sorted(Answer_dict.items(), key=operator.itemgetter(1))  # Final_Answer is a dictionary storing the clusters.
dict4 = sorted(dict4.items(), key=operator.itemgetter(1))

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Zipprs')
sheet1.write(0, 1, 'Y')
sheet1.write(0, 2, 'X')
sheet1.write(0, 3, 'clusterNo')
sheet1.write(0, 4, 'clusterName')
sheet1.col(0).width = 5000
sheet1.col(1).width = 5000
sheet1.col(2).width = 5000
sheet1.col(3).width = 5000
for i in range(len(zipprs)):
    sheet1.write(i + 1, 0, zipprs[i])
for i in range(len(Y)):
    sheet1.write(i + 1, 1, Y[i])
    sheet1.write(i + 1, 2, X[i])
    sheet1.write(i + 1, 3, Answer_dict[clstrwith4[i]])
    sheet1.write(i + 1, 4, Clusterlist[Answer_dict[clstrwith4[i]] - 1])
wb.save('Result91k20.csv')
