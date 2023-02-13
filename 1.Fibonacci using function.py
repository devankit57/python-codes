
def fibo(n):
    
    if (n==0 or n==1):
        return n
    
    return fibo(n-1)+fibo(n-2) #Recursive Case
for n in range(0,15):
    print(fibo(n),"  ",end='')

