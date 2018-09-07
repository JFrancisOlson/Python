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
        
    

                    

print("             Financial Analysis              ")
print("_____________________________________________")
print("")
print("Total months: "+ str(row_count))

    for row[1] in csvreader:
        Total=0+float(row[1])
        Total=(float(row+next(row))print("")
print("Total:        $" + Total)



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
    
