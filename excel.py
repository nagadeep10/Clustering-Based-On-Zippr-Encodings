import xlrd
from xlwt import Workbook
import operator
path = "D:/VMC_spread_data.csv"
book = xlrd.open_workbook(path)

limit =200
k=5
k1=1
k2=0.05

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

def distance(a,b):
    l=0
    templista=[]
    templistb=[]
    for i in range(len(a)):
        if(a[i].isalpha()):
            templista.append(ord(a[i])-55)
            continue
        else:
            templista.append(int(a[i]))
    for i in range(len(b)):
        if(b[i].isalpha()):
            templistb.append(ord(b[i])-55)
            continue
        else:
            templistb.append(int(b[i]))
    count=36**3
    val1=0
    val2=0
    for i in range(len(templista)):
        val1+=count*templista[i]
        val2+=count*templistb[i]
        count/=36
    return abs(val1-val2)


def generatedist3(List1):
    dist=[]
    for i in range(len(List1)):
        list2=[]
        for j in range(len(List1)):
            if i==j:
                list2.append(10000000000)
            else:
                list2.append(int(k1*(dict3[List1[i]]+dict3[List1[j]])+k2*distance(List1[i],List1[j])))
        dist.append(list2)
    return dist


def generatedist4(List1):
    dist=[]
    for i in range(len(List1)):
        list2=[]
        for j in range(len(List1)):

            if i==j:
                list2.append(10000000000)
            else:
                list2.append(int(k1*(dict4[List1[i]]+dict4[List1[j]])+k2*distance(List1[i],List1[j])))
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
            if(dist[i][j]<Min):
                Ii=i
                Ji=j
                Min=dist[i][j]
    return (Ii,Ji)

c2=len(dict2)
c3=len(dict3)
c4=len(dict4)
print c2
print c3
print c4

if  k>100000000:
    NameList = []
    Clusterdict = {}
    answerDict = {}
    for i in dict3:
        NameList.append(i)
    NameList.sort()
    print dict3
    print NameList
    # print len(dict3)

    DupNameList=NameList
    DupDict3=dict3

    for i in range(len(NameList)):
        tem_list = []
        tem_list.append(NameList[i])
        answerDict[NameList[i]]=tem_list

    # print answerDict
    dist = generatedist3(NameList)
    for _ in range(c3-k):
        x,y = getMin(dist)
        # print x,y
        # print NameList[x],NameList[y]
        if NameList[x]=="Spam" or NameList[y]=="Spam":
            continue;
        if(dict3[NameList[x]]>dict3[NameList[y]]):
            dict3[NameList[x]]+=dict3[NameList[y]]
            for i in range(len(NameList)):
                dist[i][y] = 10000000000
                dist[y][i] = 10000000000
            answerDict[NameList[x]].extend(answerDict[NameList[y]])
            del answerDict[NameList[y]]
            NameList[y]="Spam"
            # del dict3[NameList[y]]
        else:
            dict3[NameList[y]]+=dict3[NameList[x]]
            for i in range(len(DupNameList)):
                dist[i][x] = 10000000000
                dist[x][i] = 10000000000
            answerDict[NameList[y]].extend(answerDict[NameList[x]])
            del answerDict[NameList[x]]
            NameList[x] = "Spam"
            # del dict3[NameList[x]]

    Clusterlist = answerDict.keys()
    Clusterlist.sort()
    # print Clusterlist

    Final_Answer = sorted(answerDict.items(),
                          key=operator.itemgetter(1))  # Final_Answer is a list storing the clusters.
    # print len(Final_Answer)
    # print Final_Answer

    Answer_dict = {}
    for i in range(len(DupNameList)):
        Answer_dict[DupNameList[i]] = 0
    for i in range(k):
        templist = []
        templist = Final_Answer[i][1]
        for j in range(len(templist)):
            Answer_dict[templist[j]] = i + 1

    asdf = sorted(Answer_dict.items(), key=operator.itemgetter(1))  # Final_Answer is a dictionary storing the clusters.
    print asdf
    dict3 = sorted(dict3.items(),key=operator.itemgetter(1))
    print dict3

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Zipprs')
    sheet1.write(0, 1, 'Y')
    sheet1.write(0, 2, 'X')
    sheet1.write(0, 3, 'clusterNo')
    sheet1.col(0).width = 5000
    sheet1.col(1).width = 5000
    sheet1.col(2).width = 5000
    sheet1.col(3).width = 5000
    for i in range(len(zipprs)):
        sheet1.write(i + 1, 0, zipprs[i])
    for i in range(len(Y)):
        sheet1.write(i + 1, 1, Y[i])
        sheet1.write(i + 1, 2, X[i])
        sheet1.write(i + 1, 3, Answer_dict[clstrwith3[i]])
        sheet1.write(i + 1, 4, Clusterlist[Answer_dict[clstrwith3[i]] - 1])
    wb.save('k_0.05_3.csv')

#for merging 4th lvl clusters
else:
    NameList = []
    Clusterdict = {}
    answerDict = {}
    for i in dict4:
        NameList.append(i)
    NameList.sort()
    # print dict3
    # print NameList
    # print len(dict3)

    DupNameList = NameList
    DupDict4 = dict4

    for i in range(len(NameList)):
        tem_list = []
        tem_list.append(NameList[i])
        answerDict[NameList[i]] = tem_list

    # print answerDict
    dist = generatedist4(NameList)
    for _ in range(c4 - k):
        x, y = getMin(dist)
        # print x, y
        # print NameList[x], NameList[y]
        if NameList[x] == "Spam" or NameList[y] == "Spam":
            continue;
        if (dict4[NameList[x]] > dict4[NameList[y]]):
            dict4[NameList[x]] += dict4[NameList[y]]
            for i in range(len(NameList)):
                dist[i][y] = 10000000000
                dist[y][i] = 10000000000
            answerDict[NameList[x]].extend(answerDict[NameList[y]])
            del answerDict[NameList[y]]
            NameList[y] = "Spam"
            # del dict3[NameList[y]]
        else:
            dict4[NameList[y]] += dict4[NameList[x]]
            for i in range(len(DupNameList)):
                dist[i][x] = 10000000000
                dist[x][i] = 10000000000
            answerDict[NameList[y]].extend(answerDict[NameList[x]])
            del answerDict[NameList[x]]
            NameList[x] = "Spam"
            # del dict3[NameList[x]]

    Clusterlist = answerDict.keys()
    Clusterlist.sort()
    # print Clusterlist

    Final_Answer = sorted(answerDict.items(),
                          key=operator.itemgetter(1))  # Final_Answer is a list storing the clusters.
    # print len(Final_Answer)
    print Final_Answer
    Answer_dict = {}
    for i in range(len(DupNameList)):
        Answer_dict[DupNameList[i]] = 0
    for i in range(k):
        templist = []
        templist = Final_Answer[i][1]
        for j in range(len(templist)):
            Answer_dict[templist[j]] = i + 1

    asdf = sorted(Answer_dict.items(), key=operator.itemgetter(1))  # Final_Answer is a dictionary storing the clusters.
    print asdf
    dict4 = sorted(dict4.items(), key=operator.itemgetter(1))
    print dict4

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Zipprs')
    sheet1.write(0, 1, 'Y')
    sheet1.write(0, 2, 'X')
    sheet1.write(0, 3, 'clusterNo')
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
    wb.save('k_0.05_4.csv')

