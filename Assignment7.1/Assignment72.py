# Use the file name mbox-short.txt as the file name
# Using Python 3.x 
try:
    #fname = input("Enter file name: ")
    fname = "mbox-short.txt"
    fh = open(fname, "r")
except :
    print("Invalid File Name", fname)
    exit
else :
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below.   
    lcount = 0
    avg_value = 0
    sum_value = 0
    lvalue = 0.0
     
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        lcount = lcount + 1
        #print( line.rstrip())
        for f in line.split(":"):
            try:
                lvalue = float(f)
                sum_value = sum_value + lvalue 
            except:
                continue
                 
        #print( lvalue)    
                
    print( "Number of Lines: ", lcount)
    avg_value = sum_value / lcount 
    print( "Average spam confidence:", avg_value)