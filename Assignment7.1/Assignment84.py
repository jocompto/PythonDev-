# Use the file name romeo.txt as the file name
# Using Python 3.x 
# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
try:
    #fname = input("Enter file name: ")
    fname = "romeo.txt"
    fh = open(fname, "r")
except :
    print("Invalid File Name", fname)
    exit
else :
# Create empty lists to hold words from the file and list of unique words  
    lst = list()
    ulst = list()
# for each line in the file,  split it into a list  and sort it for quicker processing     
    for line in fh:
        lst = line.split()
        lst.sort()
        for word in lst:
            if word not in ulst:
                ulst.append(word)
                ulst.sort()
                        
    
    print( "Unique Words:", ulst)
    