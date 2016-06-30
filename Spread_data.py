import random
from pymongo import MongoClient

client=MongoClient ()
db =client.vmcdb
collection=db.vmcol

pre_list=[(obj.setdefault('roadNo'," "),obj.setdefault('location', " "), obj.setdefault('zippr', " "))for obj in db.vmcol.find()]
print len(pre_list)
Road_no=[]
location=[]
zippr=[]
for i in range(len(pre_list)):
    if pre_list[i] != " " and pre_list[i] != None and pre_list[i] != "":
        Road_no.append(pre_list[i][0])
        location.append(pre_list[i][1]['coordinates'])
        zippr.append(pre_list[i][2])

num=[]
ans0=[]
ans1=[]
ans2=[]
num=random.sample(range(1,len(Road_no)),200)
print num
for i in range(len(num)):
    ans0.append(Road_no[num[i]])
    ans1.append(location[num[i]])
    ans2.append(zippr[num[i]])


from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Zipprs')
sheet1.write(0, 1, 'Longitudes')
sheet1.write(0, 2, 'Latitudes')

sheet1.col(0).width = 5000
sheet1.col(1).width = 7000
sheet1.col(2).width = 7000

for i in range(len(ans0)):
    sheet1.write(i + 1, 0, ans2[i])

for i in range(len(ans1)):
    sheet1.write(i + 1, 1, ans1[i][1])
    sheet1.write(i + 1, 2, ans1[i][0])
for i in range(len(ans2)):
    sheet1.write(i+1,3,ans0[i])

wb.save('VMC_spread_data.csv')  # your code goes here