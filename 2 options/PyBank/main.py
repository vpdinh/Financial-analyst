import os
import csv

pathfile = open("raw_data/budget_data_2.csv",'r')
csvdata = csv.DictReader(pathfile)

totalrev = [] # Create a list to store every single month's revenue
average = [] # create a list to calculate average change by months over entire prior
date=[] # create a list to store months, to look up Date for greatest increase and decrease
totalrevenue=0 #Count total revenue 
#Fetching data from file to lists
for data in csvdata:
    totalrevenue = totalrevenue + int(data['Revenue'])
    totalrev.append(int(data['Revenue']))
    date.append(data['Date'])

#Calculate change by months by get next month subtract current month or vice versa
end=len(totalrev)-1
listindex = [] #To store previous Index for look up the Date after calculate average change
while end >0:
    average.append(totalrev[end]-totalrev[end-1]) 
    #create a list to store index   
    listindex.append(end)
    end=end-1

indmax=0 # To Look up for index of max value(Greatest increase)
max1 = 0 # To look up max value(Greatest increase)
min1 = 0 # To look up max value(Greatest decrease)
indexmin=0 #To Look up for index of max value(Greatest decrease)
i=len(average)-1
#for index1 in range(len(average)-1):
while i >= 0:
    if max1 <= average[i]:
        max1 = average[i]
        indexmax = listindex[i]
    if min1 >=average[i]:
        min1=average[i]
        indexmin=listindex[i]
    i=i-1

print("```")
print("Financial Analysis")
print("-"*30)
print("Total Month:" + " " + str(len(totalrev)))
print("Total Revenue:"+" " + str(totalrevenue))
print("Average Revenue Change:" + " " + str(sum(average)/len(totalrev)))
print("Greatest Increase in Revenue:" + " " + date[indexmax] + " " + "("+"$"+ str(max1)  + ")")
print("Greatest Decrease in Revenue:" + " " + date[indexmin] + " " + "("+"$"+ str(min1)  + ")")
print("```")

file = open('PyBank.txt','a') 
file.write("```\n") 
file.write("Financial Analysis \n") 
file.write("-"*30+"\n") 
file.write("Total Month:" + " " + str(len(totalrev))+"\n")
file.write("Total Revenue:"+" " + str(totalrevenue)+"\n")
file.write("Average Revenue Change:" + " " + str(sum(average)/len(totalrev))+"\n")
file.write("Greatest Increase in Revenue:" + " " + date[indexmax] + " " + "("+"$"+ str(max1)  + ")"+"\n")
file.write("Greatest Decrease in Revenue:" + " " + date[indexmin] + " " + "("+"$"+ str(min1)  + ")"+"\n")
file.write ("```\n")
file.close() 