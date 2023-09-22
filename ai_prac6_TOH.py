#Tower of Hanoi ====================
def TowerOfHanoi(n , a, b, c):
    if n==1:
        print ("Move disk 1 from source",a,"to destination",b)
        return
    TowerOfHanoi(n-1, a, c, b)
    print ("Move disk",n,"from source",a,"to destination",b)
    TowerOfHanoi(n-1, c, b, a)
         
# Driver code
TowerOfHanoi(3,'A','C','B')
    
