# Use words.txt as the file name
# Using Python 3.x 
try:
    fname = input("Enter file name: ")
    fh = open(fname, "r")
except :
    print("Invalid File Name", fname)
    exit
else :    
    for line in fh:
        line = line.upper()
        print( line.rstrip())    