# Import the csv module to read the csv file
# Import the os file to join with the path and make it independent of os type
import csv
import os
import string

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row)
    # skips the header row and counts the number of months
        row_count = sum(1 for row in csvreader) 

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

pnl_delta_List=[]
for value in pnl_List:
    this_pnl=row[value]
    next_pnl=next(row[value])
    delta_value=this_pnl-next_pnl
    pnl_delta_List.append(delta_value)
print(pnl_delta_List)
#for value in pnl_delta:


# Print the form to the terminal            

print("             Financial Analysis              ")
print("_____________________________________________")
print("")
print("Total months: "+ str(row_count))
print("")
print("Total:        $" + str(pnl_sum))



  #  print(csvreader)

    # Read the header row first (skip this step if there is no header)
   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #print(row)
    
