# Import the csv os string itertools and operator modules
import csv
import os
import string
import itertools
import operator

# map the path to the data
csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
      #  print(row)
    # skips the header row and counts the number of months
        row_count = sum(1 for row in csvreader) 



with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    
    next(csvreader) # Skip header
    
    data=[r for r in csvreader]

#print(data)
pnl_List=[]
for row in data:
    pnl_List.append(row[1])
#print(pnl_List)

# Sum the revenues its a list so it has to be converted to a number format
pnl_sum = 0
for value in pnl_List:
    pnl_sum += float(value)
#print(pnl_sum)

# Convert entire pnl_List data set from string to integer.
pnl_List = list(map(int, pnl_List))

def differences(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            yield (nums[i]-nums[j])

delta_List=[]
for d in differences(pnl_List): 
    
   # append delta list (d)
    delta_List.append(d)

# Sum the difference in revenues its a list so it has to be converted to a number format
delta_sum = 0
for value in delta_List:
    delta_sum += value
    avg_delta=(delta_sum)/85
#print(str(avg_delta))

# Verify conversion
#print(pnl_List)

# Print the form to the terminal            

print("             Financial Analysis              ")
print("_____________________________________________")
print("")
print("Total months:                " + str(row_count))
print("")
print("Total:                      $" +str(pnl_sum))
print("")
print("The average change           " +str(avg_delta))
print("")
print("Greatest increase in profits " +str(delta_List.index(max(delta_List))))
print("")
print("Greatest decrease in profits " +str(delta_List.index(min(delta_List))))