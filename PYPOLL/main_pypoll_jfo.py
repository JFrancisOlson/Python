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

with open(csvpath, newline='') as csvfile:
# CSV reader specifies the delimiter and variable that holds contents
    Poll_data = csv.reader(csvfile,delimiter=',')
    
 # Loop through looking for the video
    for row in Poll_data:
        if row[2] == "Kahn":
            row_count=int(sum(1 for row in Poll_data))
            Kahn_count=row_count
        elif row[2] == "Correy":
            row_count=int(sum(1 for row in Poll_data))
            Correy_count=row_count
        elif row[2] == "Li":
            row_count=int(sum(1 for row in Poll_data))
            Li_count=row_count
        elif row[2] == "O'Tooley":
            row_count=int(sum(1 for row in Poll_data))
            OTooley_count=row_count

#            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
#            found = True

    #if Kahn_count > Correy_count and Kahn_count > Li_count and Kahn_count>OTooley_count:





print("             Electiion Results               ")
print("_____________________________________________")
print("")
print("Total Votes:           " + str(row_count))
print("")
print("_____________________________________________")
print("")
print("Kahn:                  " + str(Kahn_count))
print("")
print("")
print("Correy:                " + str(Correy_count))
print("")
print("")
print("Li:                    " + str(Li_count))
print("")
print("")
print("O'Tooley:              " + str(OTooley_count))
print("")
print("_____________________________________________")
print("")
print("Winner:                " + str(OTooley_count))
print("")

