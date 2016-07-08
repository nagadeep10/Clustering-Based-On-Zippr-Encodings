import random
import math
import googlemaps
import responses


n=15#number of cities
m=3#number of salesmen
chrom=n


# Distance matrix  from excel and google matrix
# import xlrd
# path = "G:/Data.xlsx"
# book = xlrd.open_workbook(path)
# first_sheet = book.sheet_by_index(0)
# Zipprs = first_sheet.col_values(0)
# del Zipprs[0]
# Longitudes = first_sheet.col_values(1)
# del Longitudes[0]
# Latitudes = first_sheet.col_values(2)
# del Latitudes[0]
# list=[]
# for i in range(n):
#      pp=(Longitudes[i],Latitudes[i])
#      list.append(pp)
# key = 'AIzaSyCruXmNIiJWkh8zKsE50dQwExcAegLeMhs'
# client = googlemaps.Client(key)
# responses.add(responses.GET,
#               'https://m...content-available-to-author-only...s.com/maps/api/distancematrix/json',
#               body='{"status":"OK","rows":[]}',
#               status=200,
#               content_type='application/json')
# googlematrix = client.distance_matrix(list, list)
# matrix=[]
# dist=[]
# templist=[]
# for i in range(n):
#     for j in range(n):
#        templist.append(str(googlematrix[u'rows'][i][u'elements'][j][u'distance'][u'text']))
#     matrix.append(templist)
#     templist=[]
# Maximum=-1
# templist=[]
# for i in range(n):
#     for j in range(n):
#         temp=matrix[i][j]
#         length=len(temp)
#         if temp[length-2]=='k':
#             Maximum=max(Maximum,float(temp[0:length-3]))
#             templist.append(float(temp[0:length-3]))
#         else:
#             templist.append(0)
#     dist.append(templist)
#     templist=[]
# floatMatrix=[]
# templist=[]
# for i in range(n):
#     for j in range(n):
#         templist.append(dist[i][j]/Maximum)
#     floatMatrix.append(templist)
#     templist=[]
#
# for r in dist:
#     print r

dist=[[0,29,82,46,68,52,72,42,51,55,29,74,23,72,46],[29,0,55,46,42,43,43,23,23,31,41,51,11,52,21],[82,55,0,68,46,55,23,43,41,29,79,21,64,31,51],[46,46,68,0,82,15,72,31,62,42,21,51,51,43,64],
      [68,42,46,82,0,74,23,52,21,46,82,58,46,65,23],[52,43,55,15,74,0,61,23,55,31,33,37,51,29,59],[72,43,23,72,23,61,0,42,23,31,77,37,51,46,33],[42,23,43,31,52,23,42,0,33,15,37,33,33,31,37],
      [51,23,41,62,21,55,23,33,0,29,62,46,29,51,11],[55,31,29,42,46,31,31,15,29,0,51,21,41,23,37],[29,41,79,21,82,33,77,37,62,51,0,65,42,59,61],[74,51,21,51,58,37,37,33,46,21,65,0,61,11,55],
      [23,11,64,51,46,51,51,33,29,41,42,61,0,62,23],[72,52,31,43,65,29,46,31,51,23,59,11,62,0,59],[46,21,51,64,23,59,33,37,11,37,61,55,23,59,0]]
for r in dist:
  print(r)
ans=0
first = []
second = []

def GenerateRandom(num):
    for _ in range(num):
        first.append(random.sample(range(1, n + 1), n))
    for tt in range(num):
        list = []
        tempsum = 0;
        for xx in range(m - 1):
            list.append(random.randint(1, n-m))
            tempsum = tempsum + list[xx]
        for xx in range(len(list)):
            list[xx] = int((list[xx] * (n - 1)) / tempsum)
        tempsum = 0
        for xx in range(len(list)):
            tempsum = tempsum + list[xx]
        list.append(n - tempsum)
        list.append(-1)
        print list
        second.append(list)
num_loops=1000

def fitness(first,second):
        temp = 0
        fit = []
        ans = -(2 ** 30)
        for i in range(len(second)):
            start = 1
            ans = -(2 ** 30)
            if second[i][m] == -1:
                # print ans
                for j in range(m):
                    # print i,j,ans
                    # print

                    temp = 0
                    for k in range(start,start+second[i][j]-1):
                        # print k,second[i][j]
                        #print i,k
                        if k==10:
                            print second[i]
                        temp += dist[first[i][k-1]-1][first[i][k]-1]
                    if temp>ans:
                        ans=temp
                    # print ans,temp
                    # print
                    start += second[i][j]
                if ans != 0:
                        ans = 90000/ans
                second[i][m] = ans
                fit.append(ans)
            else:
                fit.append(second[i][m])
        return fit
def crossover1(first,second):
        for _ in range(chrom/2):
            i1 = random.randint(0,chrom-1)
            i2 = random.randint(0,chrom-1)
            while(i1==i2):
                i2 = random.randint(0, chrom - 1)
            j1 = random.randint(0, n - 1)
            j2 = random.randint(0, n - 1)
            while (j1 == j2):
                j2 = random.randint(0, n - 1)
            dict1={}
            dict2={}
            secondlist1 = []
            secondlist2 = []
            anslist1 = []
            anslist2 = []
            for i in range(n):
                anslist1.append(first[i1][i])
                dict1[first[i1][i]]=i
            for i in range(n):
                anslist2.append(first[i2][i])
                dict2[first[i2][i]] = i
            for i in range(m+1):
                secondlist1.append(second[i1][i])
                secondlist2.append(second[i2][i])
            l1=[]
            l2=[]
            for j in range(j1,j2):
                l1.append(dict2[first[i1][j]])
            for j in range(j1, j2):
                l2.append(dict1[first[i2][j]])
            l1.sort()
            l2.sort()
            p=0
            for j in range(j1, j2):
                anslist1[j] = first[i2][l1[p]]
                anslist2[j] = first[i1][l2[p]]
                p=p+1
            first.append(anslist1)
            first.append(anslist2)
            second.append(secondlist1)
            second.append(secondlist2)
        return
def crossover2(first,second):
        for _ in range(chrom/ 2):
            i1 = random.randint(0, chrom - 1)
            i2 = random.randint(0, chrom - 1)
            while (i1 == i2):
                i2 = random.randint(0, chrom - 1)
            j1 = random.randint(0, n - 1)
            dict1 = {}
            dict2 = {}
            anslist1 = []
            anslist2 = []
            secondlist1 = []
            secondlist2 = []
            for i in range(n):
                anslist1.append(first[i1][i])
                dict1[first[i1][i]] = i
            for i in range(n):
                anslist2.append(first[i2][i])
                dict2[first[i2][i]] = i
            for i in range(m+1):
                secondlist1.append(second[i1][i])
                secondlist2.append(second[i2][i])
            temp=first[i1][j1]
            num=0;pos=j1
            crosslist=[]
            crosslist.append(j1)
            while(num!=temp):
                num=anslist2[pos]
                pos=dict1[num]
                crosslist.append(pos)
            for i in range(len(crosslist)-1):
                p=crosslist[i]
                temp=anslist1[p]
                anslist1[p]=anslist2[p]
                anslist2[p]=temp
            first.append(anslist1)
            first.append(anslist2)
            second.append(secondlist1)
            second.append(secondlist2)
        return
def crossover3(first,second):
        for _ in range(chrom/ 2):
            i1 = random.randint(0, chrom - 1)
            i2 = random.randint(0, chrom - 1)
            while (i1 == i2):
                i2 = random.randint(0, chrom - 1)
            anslist1 = []
            anslist2 = []
            p1=[]
            p2=[]
            alpha=random.uniform(0, 1)
            for i in range(m):
                p1.append(second[i1][i])
                p2.append(second[i2][i])
                temp1=alpha*second[i1][i]+(1-alpha)*second[i2][i]
                temp1=math.floor(temp1)
                temp2 = alpha * second[i2][i] + (1 - alpha) * second[i1][i]
                temp2 = math.floor(temp2)
                anslist1.append(temp1)
                anslist2.append(temp2)
            tempsum1=0;tempsum2=0
            for i in range(m):
                tempsum1 = tempsum1+anslist1[i]
                tempsum2 = tempsum2 + anslist2[i]
            list = []
            lost = []
            last = []
            tempsum = 0;
            for xx in range(m - 1):
                list.append(random.randint(1, 100000000))
                lost.append(0)
                last.append(0)
                tempsum = tempsum + list[xx]
            for xx in range(len(list)):
                last[xx] = int((list[xx] * (n-tempsum1)) / tempsum)
                lost[xx] = int((list[xx] * (n-tempsum2)) / tempsum)
            tempsum = 0
            tempsum0 = 0
            for xx in range(len(last)):
                tempsum = tempsum + last[xx]
                tempsum0 += lost[xx]
            last.append(n - tempsum1-tempsum)
            lost.append(n - tempsum2-tempsum)
            for i in range(m):
                anslist1[i]+=last[i]
                anslist1[i]=int(anslist1[i])
                anslist2[i]+=lost[i]
                anslist2[i] = int(anslist2[i])
            anslist1.append(-1)
            anslist2.append(-1)
            firstlist1 = []
            firstlist2 = []
            for i in range(n):
                firstlist1.append(first[i1][i])
                firstlist2.append(first[i2][i])
            first.append(firstlist1)
            first.append(firstlist2)
            second.append(anslist1)
            second.append(anslist2)
        return
def mutation1(first,second):
    count = 0
    for x in range(chrom/2):

        po = random.randint(0, n-1)
        op = random.randint(0, n-1)
        while(po==op):
            op = random.randint(0, n - 1)
        j=max(po,op)
        i=min(po,op)
        part1 = []
        part2 = []
        for a in range(n):
            part1.append(first[x][a])
        for b in range(m+1):
            part2.append(second[x][b])
        for y in range(i,(j+i)/2+1):
            temp=part1[y]
            part1[y]=part1[i+j-y]
            part1[i+j-y]=temp
        # print i,j
        count += 1
        #chr += 1
        first.append(part1)
        second.append(part2)
    return
def mutation2(first,second):
    for _ in range(chrom / 2):
        x=random.randint(0,chrom-1)
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        part1 = []
        part2 = []
        for a in range(n):
            part1.append(first[x][a])
        for b in range(m+1):
            part2.append(second[x][b])
        temp = part1[i]
        part1[i] = part1[j]
        part1[j] = temp
        first.append(part1)
        second.append(part2)
    return
def mutation3(first, second):
    for _ in range(chrom / 2):
        x = random.randint(0, chrom - 1)
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        while i==j:
            j = random.randint(0, n - 1)
        part1 = []
        part2 = []
        for a in range(n):
            part1.append(first[x][a])
        for b in range(m + 1):
            part2.append(second[x][b])
        alpha=random.uniform(0,1)
        sum = part2[i] + part2[j]
        part2[i] = int(part2[i] + part2[j]*alpha*0.5)
        part2[j] = sum - part2[i]
        first.append(part1)
        second.append(part2)
    return

GenerateRandom(chrom)
# for poiu in range(num_loops):
#     #Testing begin
#     mutation1(first,second)
#     mutation2(first,second)
#     mutation3(first,second)
#     crossover1(first, second)
#     crossover2(first, second)
crossover3(first,second)
for x in second:
    print x
#     chrnew=len(first)
#     Fitness=fitness(first,second)
#     #print Fitness
#     totalsum=0
#     index=0
#     tempfit = 0
#     maxfit = 0
#     temsum=[]
#     for x in range(len(Fitness)):
#         totalsum+=Fitness[x]
#         temsum.append(totalsum)
#         if Fitness[x]>maxfit:
#             maxfit=Fitness[x]
#             index=x
#     for x in range(len(Fitness)):
#         temsum[x]=temsum[x]/(float(totalsum))
#     #print maxfit,index
#     temp1= []
#     temp2= []
#     part1 = []
#     part2 = []
#     for i in range(n):
#         part1.append(first[index][i])
#     for i in range(m + 1):
#         part2.append(second[index][i])
#     if poiu == num_loops-1:
#         print part1
#         print part2
#         finalanswer=0
#         tempo=0;
#         for i in range(m):
#             if i!=0:
#                 tempo=part2[i-1]
#             for j in range(tempo+1,part2[i]+tempo-1):
#                 finalanswer+=dist[part1[j-1]-1][part1[j]-1]
#                # print finalanswer
#         #print finalanswer
#     temp1.append(part1)
#     temp2.append(part2)
#
#     for x in range(chrom-1):
#         t = random.uniform(0, 1)
#         for y in range(len(temsum)):
#             if t<temsum[y]:
#                 part1 = []
#                 part2 = []
#                 for i in range(n ):
#                     part1.append(first[y][i])
#                 for i in range(m+1):
#                     part2.append(second[y][i])
#                 temp1.append(part1)
#                 temp2.append(part2)
#                 temsum[y]=0
#                 break
#    #print maxfit
#     first=temp1
#     second=temp2
#
#     for i in range(len(second)):
#         if second[i][m]>tempfit:
#             tempfit=second[i][m]
#     print tempfit
#     ans=max(ans,maxfit)
# print ans
