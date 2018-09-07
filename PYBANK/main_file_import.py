# Store the file path associated with the pybank file
file = '../Resources/input.txt'

test_List=[]

# Open the file in 'read' mode ('r') and then store the contents in the variable bank_data
with open(file,'r') as text:
    print(text)

    # Store all the text inside a variable called "lines"
    lines = text.read()
    test_List.append(lines)
    
    # Print the contents of the text file
    print(lines)
    print(test_List)

    # Import the random and string Modules
import random
import string

# Utilize the string module's custome method: ".ascii_letters"
print(string.ascii_letters)

# Utilize the random modulle's custome method: randint
for x in range (10):
    print(random.randint(1,10))