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
Total=row_count
print("             Electiion Results               ")
print("_____________________________________________")
print("")
print("Total Votes:           " + str(row_count))
print("")

csvpath = os.path.join('..','Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    
    next(csvreader) # Skip header
    
    data=[r for r in csvreader]
    
    for row in csvreader:
        row_count = sum(1 for row in csvreader) 
    Total_Vote=3521001
    #print(data)
    candidate_List=[]
    for row in data:
        candidate_List.append(row[2])
    #print(candidate_List)
    
    khanpct=((candidate_List.count('Kahn'))/Total_Vote)
    correypct=((candidate_List.count('Correy'))/Total_Vote)

    lipct=((candidate_List.count('Li'))/Total_Vote)

    otooleypct=((candidate_List.count("O'Tooley"))/Total_Vote)

    print ("Khan:          ", str(khanpct),"%    (", candidate_List.count('Khan'),")")
    print ("Correy:       ", str(correypct),"%    (", candidate_List.count('Correy'),")")
    print ("Li:           ", str(lipct),"%    (", candidate_List.count('Li'),")")
    print ("O'Tooley:     ", str(otooleypct),"%    (", candidate_List.count("O'Tooley"),")")

    
    

