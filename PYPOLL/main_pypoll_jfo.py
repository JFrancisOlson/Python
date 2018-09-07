# Import the csv os string itertools and operator modules
import csv
import os
import string
import itertools
import operator

# map the path to the data
csvpath = os.path.join('..','Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:

    # skips the header row and counts the number of months
        row_count = sum(1 for row in csvreader) 

        print(row)

# CSV reader specifies the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    
    
print("             Electiion Results               ")
print("_____________________________________________")
print("")
print("Total Votes:                " + str(row_count))
print("")
print("_____________________________________________")