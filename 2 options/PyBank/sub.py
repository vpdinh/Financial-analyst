import os
import csv

pathfile1 = open('budget_data_1.csv','r')
pathfile2=open('budget_data_2.csv','r')
csvdata1 = csv.DictReader(pathfile1)
csvdata2 = csv.DictReader(pathfile2)
countmonth1 = '' #get month of CSV file 1
countdate1=0 #get day of CSV file 1
revenue = 0 # total revevue
maxminrevenue= [] # list of  revenue by moths to find max increase and max decrease in revenue before filter Revenue by Month of CSV file 1
listmon_1 = [] #get month in CSV file 1
listmon_2 = [] #get month in CSV file 2
list_day=[] # Because of Date stored in CSV file 1 and CSV file 2 is in different format so this list will store Day in CSV file 1 to print out when look up MAX. MIN revenue  
averagemon = []# list of  revenue by moths to find max increase and max decrease in revenue after filtered Revenue by Month of CSV file 1
newlist=[] #This list contain Revenue begin from Jan-2009 to Dec-2018 so average change monthly by pair of Jan 2009 revenue subtract Feb 2009 revenue, Mar subtract April 2009 till Dec-2009
Jan = 0
Feb = 0 
Mar=0
April=0
May=0
Jun=0
Jul=0
Aug=0
Sep=0
Oct=0
Nov=0
Dec=0
# CSV file 1 and CSV file had a different format in display of Date column so we have to deal with it in diff way 
for data1 in csvdata1:
    countmonth1,countdate1 = (str(data1['Date'])).split("-")
    listmon_1.append(countmonth1)
    list_day.append(countdate1)
    revenue = revenue + int(data1['Revenue'])
    maxminrevenue.append(int(data1['Revenue']))
    # Sum revenue by month of 2018 in Budget_data_1.csv
    if (countmonth1 =='Jan'):
        Jan=Jan+int(data1['Revenue'])
    if (countmonth1 =='Feb'):
        Feb=Feb+int(data1['Revenue'])
    if (countmonth1 =='Mar'):
        Mar=Mar+int(data1['Revenue'])
    if (countmonth1 =='April'):
        April=April+int(data1['Revenue'])
    if (countmonth1 =='May'):
        May=May+int(data1['Revenue'])
    if (countmonth1 =='Jun'):
        Jun=Jun+int(data1['Revenue'])
    if (countmonth1 =='Jul'):
        Jul=Jul+int(data1['Revenue'])
    if (countmonth1 =='Aug'):
        Aug=Aug+int(data1['Revenue'])
    if (countmonth1 =='Sep'):
        Sep=Sep+int(data1['Revenue'])
    if (countmonth1 =='Oct'):
        Oct=Oct+int(data1['Revenue'])
    if (countmonth1 =='Nov'):
        Nov=Nov+int(data1['Revenue'])
    if (countmonth1 =='Dec'):
        Dec=Dec+int(data1['Revenue'])
for data2 in csvdata2:
    listmon_2.append(data2['Date'])
    revenue = revenue+int(data2['Revenue'])
    maxminrevenue.append(int(data2['Revenue']))
    averagemon.append(int(data2['Revenue']))

#then insert these revenues of every single month of 2018 to list to calculate average change by Months
averagemon.extend([Jan,Feb,Mar,April,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec])
#Find the index of max revenue in the list
index_max = maxminrevenue.index(max(maxminrevenue))
indexmax_date=""
#If index_max is smallest total row of CSV file 1 then look up its value in CSV file 1 otherwise CSV 2
if index_max <= csvdata1.line_num:
    indexmax_date = listmon_1[index_max]+ " - " + list_day[index_max]
else:
    indexmax_date=listmon_2[index_max-csvdata1.line_num+1]
#Find the index of min revenue in the list
index_min = maxminrevenue.index(min(maxminrevenue))
indexmin_date = ""
#If index_min is smallest total row of CSV file 1 then look up its value in CSV file 1 otherwise CSV 2
if index_min <= csvdata1.line_num:
    indexmin_date= listmon_1[index_min] + " - " + list_day[index_min]
else:
    indexmin_date = listmon_2[index_min-csvdata1.line_num+1]

#Set function to remove duplicate value in 2 list,specifically to remove duplicate Month in list of CSV file 1
listmon_2 = set(listmon_2)
listmon_1 = set(listmon_1)

# This list contain Revenue begin from Jan-2009 to Dec-2018 so average change monthly by pair of Jan 2009 subtract Feb 2009 till Dec-2009
i=0
while i<=(len(averagemon)-1):
    newlist.append(averagemon[i] - averagemon[i+1])
    i=i+2

print("```")
print("Financial Analysis")
print("-"*30)
print("Total Month:" + " " + str(len(listmon_1)+len(listmon_2)))
print("Total Revenue:"+" " + str(revenue))
print("Average Revenue Change:" + " " + str(sum(newlist)/len(averagemon)))
print("Greatest Increase in Revenue:" + " " + indexmax_date + " " + "("+"$"+ str(max(maxminrevenue))  + ")")
print("Greatest Decrease in Revenue:" + " " + indexmin_date + " " + "("+"$"+ str(min(maxminrevenue))  + ")")
print("```")