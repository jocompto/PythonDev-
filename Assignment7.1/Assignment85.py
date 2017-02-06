# Use the file name romeo.txt as the file name
# Using Python 3.x 
#   Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#                     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# ?? Hint: make sure not to include the lines that start with 'From:'.
try:
    #fname = input("Enter file name: ")
    fname = "mbox-short.txt"
    fh = open(fname, "r")
except :
    print("Invalid File Name", fname)
    exit
else :
# Create empty lists to hold words from the file and list of unique words  
#    lst = list()
    count = 0  
# for each line in the file,  split it into a list  and sort it for quicker processing     
    for line in fh:
        if not line.startswith("From:") : continue 
        lst = line.split()
        count += 1
        print( lst[1] )

print("There are", count, "lines that start with From")
     