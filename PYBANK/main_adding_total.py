# Import the csv module to read the csv file
# Import the os file to join with the path and make it independent of os type
import csv
import os
import string

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    next(row)
    for row in csvreader:
        print(row)

    for row in csv.reader:
        PL_total=[]
        PL_total=append.value(row[1])   
        
       #Total=sum(1 for row[1] in csvreader)
        #numbers=[]
         #   for row[0] in csvreader:
          #  numbers.append(number)
           # Total_Revenues=sum(numbers)
            

print("             Financial Analysis              ")
print("_____________________________________________")
print("")
print("Total months: "+ str(row_count))
print("")
#print("Total:        $" + Total)


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



# fileObject is your csv.reader       
#cleaned_csv = zip(Month, Year, P_and_L, Delta_P_and_L)

#output_file = os.path.join("P_and_L.csv")



        
        

    
    # verify that the data is being imported
  #  print(csvreader)

    # Read the header row first (skip this step if there is no header)
   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #print(row)
    
