import math

n=int(input("Enter number 1 : "))
m=int(input("Enter number 2 : "))

print("The GCD of given inputs are",math.gcd(n,m))


def gcd(a,b):
    r=a%b
    while (r!=0):
        a=b
        b=r
        r=a%b
    return b

print(gcd(10764,2300) )   
