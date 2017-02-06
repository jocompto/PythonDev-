
def palgenbase2(): # generator of palindromes in base 2
    
    yield 0
    x, n, n2 = 1, 1, 2
    
    while True:
        for y in range(n, n2):
            s = format(y, 'b')
            yield int(s+s[-2::-1], 2)
        for y in range(n, n2):
            s = format(y, 'b')
            yield int(s+s[::-1], 2)
          
        x += 1
        n *= 2
        n2 *= 2 
         

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
 
def test():
    print ('Starting test')
    for char in reverse('golf'):
        print(char, end='' )
    print( '\n' )
        
def main():
   
    var = 1
    test()
    
    print('Iteration','Number', 'Binary')
    for nums, v1 in  zip(palgenbase2(), range(25)) :
         s = format(nums, 'b')
         print(v1 +1,'       ',  nums,'      ', s )
                         
    print ('ending Main')
   

if __name__ == '__main__':
    main()