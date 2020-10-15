def numpat(n):
    for i in range(1,n+1): 
        num = 1
        for k in range(1,n+1-i):
            print(end="  ")
         
        for j in range(1,i+1): 
            
             print('*', end=" ") 
             num = num + 1
        print("\r") 
            
numpat(5)            