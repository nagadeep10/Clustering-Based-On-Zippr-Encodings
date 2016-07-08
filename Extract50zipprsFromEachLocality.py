import xlrd
from xlwt import Workbook
import operator
import random
path = "D:/AH_Cluster.xlsx"
book = xlrd.open_workbook(path)

limit = 500
first_sheet = book.sheet_by_index(0)
zipprs = first_sheet.col_values(0)
zipprs = zipprs[0:limit]
del zipprs[0]
Y = first_sheet.col_values(1)
Y = Y[0:limit]
del Y[0]
X = first_sheet.col_values(2)
X = X[0:limit]
del X[0]
Road_no=first_sheet.col_values(3)
Road_no=Road_no[0:limit]
del Road_no[0]

ans0=[]
ans1=[]
ans2=[]
ans3=[]
num=random.sample(range(1,len(Road_no)),50)
print num
for i in range(len(num)):
    ans0.append(Road_no[num[i]])
    ans1.append(Y[num[i]])
    ans2.append(X[num[i]])
    ans3.append(zipprs[num[i]])


from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Zipprs')
sheet1.write(0, 1, 'Longitudes')
sheet1.write(0, 2, 'Latitudes')
sheet1.write(0,3,'Road_no')
sheet1.col(0).width = 5000
sheet1.col(1).width = 7000
sheet1.col(2).width = 7000

for i in range(len(ans0)):
    sheet1.write(i + 1, 0, ans3[i])

for i in range(len(ans1)):
    sheet1.write(i + 1, 1, ans1[i])
    sheet1.write(i + 1, 2, ans2[i])
for i in range(len(ans2)):
    sheet1.write(i+1,3,ans0[i])

wb.save('AH_CLuster_50.csv')
