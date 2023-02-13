def fib(n):
    a,b=0,1
    count=0
 
    while count<n:
         print(a)
         nth=a+b
       
         a,b=b,nth
         count+=1
fib(10)
