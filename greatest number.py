a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if (a>b and a>c):
    print(a,"is the greatest number")
    print(a,"is greater than",b,"by ",a-b)
    print(a,"is greater than",c,"by ",a-c)

elif(b>c):
    print(b,"is the greatest number")
    print(b,"is greater than",c,"by ",b-c)
    print(b,"is greater than",a,"by ",b-a)

else:
    print(c,"is the greatest number")   
    print(c,"is greater than",b,"by ",c-b)
    print(c,"is greater than",a,"by ",c-a) 


