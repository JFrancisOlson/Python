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
    
    pcnt_List=[]
    cand_List=["Khan","Correy","Li","O'Tooley"]
    
    khanpct=(int(candidate_List.count('Khan'))/int(Total_Vote))
    pcnt_List.append(str(khanpct))

    correypct=(int(candidate_List.count('Correy'))/int(Total_Vote))
    pcnt_List.append(str(correypct))
    
    lipct=(int(candidate_List.count('Li'))/int(Total_Vote))
    pcnt_List.append(str(lipct))

    otooleypct=(int(candidate_List.count("O'Tooley"))/int(Total_Vote))
    pcnt_List.append(str(otooleypct))


    print ("Khan:          ", str(khanpct),"%    (", candidate_List.count('Khan'),")")
    print("")
    print ("Correy:       ", str(correypct),"%    (", candidate_List.count('Correy'),")")
    print("")
    print ("Li:           ", str(lipct),"%    (", candidate_List.count('Li'),")")
    print("")
    print ("O'Tooley:     ", str(otooleypct),"%    (", candidate_List.count("O'Tooley"),")")
    
    print("_____________________________________________")
    print("")
    if khanpct>correypct and khanpct>lipct and khanpct>otooleypct:
        print("Winner:          Khan")
    elif  correypct>khanpct and correypct>lipct and  correypct>otooleypct:
        print("Winner:          Correy")
    elif  li>khanpct and lipct>correypct and  lipct>otooleypct:
        print("Winner:          Li")
    elif  otooleypct>khanpct and otooleypct>lipct and  otooleypct>correypct:
        print("Winner:          O'Tooley")

    #print(pcnt_List)
    
    

