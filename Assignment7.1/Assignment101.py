# Using Python 3.x 
#   Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#                     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# ?? Hint: make sure not to include the lines that start with 'From:'.
try:
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fh = open(name, "r")
except :
    print( "Invalid File Name", name )
    exit
else :
# Create empty lists to hold words from the file and list of unique words  
    lst1 = list()
    lst2 = list()
    count = dict()  
# for each line in the file,  split it into a list  and sort it for quicker processing     
    for line in fh:
        if not line.startswith("From ") : continue 
        lst1 = line.split()
        lst2 = lst1[5].split(':')
        count[lst2[0]] = count.get(lst2[0],0) + 1
        
    histogram =  sorted([(k, v) for k, v in count.items()] )
    for tup in histogram:
        print( tup[0], tup[1] )
