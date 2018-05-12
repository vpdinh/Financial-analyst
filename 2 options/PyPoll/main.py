import os
import csv

pathfile1 = open("raw_data/election_data_2.csv",'r')
#pathfile2=open('election_data_2.csv','r')
csvdata1 = csv.DictReader(pathfile1)
#csvdata2 = csv.DictReader(pathfile2)
count_vote = 0
list_cand = []
for data1 in csvdata1:
    count_vote= count_vote + 1
    list_cand.append(data1['Candidate'])
#for data2 in csvdata2:
 #   count_vote= count_vote+1
  #  list_cand.append(data2['Candidate'])

#Create a list of  candidates's name before  counting the winner
listc=[]
i=0
while i<=len(list_cand)-1:
    if list_cand[i] not in listc:
        listc.append(list_cand[i])
    i = i+1
file = open("PyPoll.txt",'a') #output file named PyPoll.text contain the result of election
print ("```")
print("Election Results")
print("-"*30)
print("Total Votes:" + " " + str(count_vote))
print("-"*30)

file.write("``` \n")
file.write("Election Results \n")
file.write("-"*30 +"\n")
file.write("Total Votes:" + " " + str(count_vote)+"\n")
file.write("-"*30 +"\n")

ind=0 # To Look up for index of winner
max1 = list_cand.count(listc[0]) # To look up winner name

for index,can in enumerate(listc):
    if max1 <= list_cand.count(listc[index]):
        ind=index
        max1 = list_cand.count(listc[index])
    print(can +":"+ " " + str("%0.1f" % (list_cand.count(can)/count_vote*100)) +  "%" + " " + "("+str(list_cand.count(can))+")")
    file.write(can +":"+ " " + str("%0.1f" % (list_cand.count(can)/count_vote*100)) +  "%" + " " + "("+str(list_cand.count(can))+")" +"\n")

print("-"*30)
print("Winner:" + " " + listc[ind])
print("-"*30)
print ("```")

file.write("-"*30+"\n")
file.write("Winner:" + " " + listc[ind]+"\n")
file.write("-"*30+"\n")
file.write("``` \n")
file.close()