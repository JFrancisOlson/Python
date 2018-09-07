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
row_count = 0
deltaList=[]
for row in csvreader:
	value = row[1]
	if row_count > 1:
		difference = previous - value
	previous = value
	delta_List.append(difference)
	row_count = 1