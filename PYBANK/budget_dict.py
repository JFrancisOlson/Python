# Import the csv module to read the csv file
# Import the os file to join with the path and make it independent of os type
import csv
import os
import string

csvpath = os.path.join('..','Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    data=[r for r in reader]
   
#print(data)
print("this is the first month data " + data[0]['Profit/Losses'])

pnl=[]
for row in data:
    pnl.append(int([0]['Profit/Losses']))

print(pnl)