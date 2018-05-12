import os
import csv

pathfile = open("raw_data/budget_data_1.csv",'r')
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
while end >0:
    average.append(totalrev[end]-totalrev[end-1])    
    end=end-1

indmax=0 # To Look up for index of max value(Greatest increase)
max1 = 0 # To look up max value(Greatest increase)
min1 = 0 # To look up max value(Greatest decrease)
indexmin=0 #To Look up for index of max value(Greatest decrease)
for index1 in range(len(totalrev)-1):
    if max1 <= totalrev[index1]:
        max1 = totalrev[index1]
        indexmax=index1
    if min1 >=totalrev[index1]:
        min1=totalrev[index1]
        indexmin=index1
    
#Simple ways by reusing build-in functions: max,min, sum on the list contain Revenue to come out the results        
#indexmax = totalrev.index(max(totalrev))
#indexmin = totalrev.index(min(totalrev))

print("```")
print("Financial Analysis")
print("-"*30)
print("Total Month:" + " " + str(len(totalrev)))
print("Total Revenue:"+" " + str(totalrevenue))
print("Average Revenue Change:" + " " + str(sum(average)/len(average)))
print("Greatest Increase in Revenue:" + " " + date[indexmax] + " " + "("+"$"+ str(max1)  + ")")
print("Greatest Decrease in Revenue:" + " " + date[indexmin] + " " + "("+"$"+ str(min1)  + ")")
print("```")

file = open('PyBank.txt','a') 
file.write("```\n") 
file.write("Financial Analysis \n") 
file.write("-"*30+"\n") 
file.write("Total Month:" + " " + str(len(totalrev))+"\n")
file.write("Total Revenue:"+" " + str(totalrevenue)+"\n")
file.write("Average Revenue Change:" + " " + str(sum(average)/len(average))+"\n")
file.write("Greatest Increase in Revenue:" + " " + date[indexmax] + " " + "("+"$"+ str(max1)  + ")"+"\n")
file.write("Greatest Decrease in Revenue:" + " " + date[indexmin] + " " + "("+"$"+ str(min1)  + ")"+"\n")
file.write ("```\n")
file.close() 