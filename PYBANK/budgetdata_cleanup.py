# Import the csv module to read the csv file
# Import the os file to join with the path and make it independent of os type
import csv
import os
import string

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    
    next(csvreader) # Skip header
    
    data=[r for r in csvreader]
    data.pop(0)
#print(data)
pnl_List=[]
for row in data:
    pnl_List.append(row[1])

#print(pnl_List)

# Sum the revenues its a list so it has to be converted to a number format
pnl_sum = 0
for value in pnl_List:
    pnl_sum += float(value)
print(pnl_sum)

#pnl_max=0
#for value in pnl_List:
 #   pnl_max=float(value)
 #   if value > pnl_max:
 #       pnl_max=(value)
#print(pnl_max)

#print("min value element : " min(float(pnl_List)[1])

#pnl_delta