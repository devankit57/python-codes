number=int(input("Enter a number to check : "))
count=0
val=int(number/2)
for i in range(2,val+1):
    div=number%i
    if (div==0):
        count=count+1

if (count>=1):
    print(number,"is not a prime number")


else:
    print(number,"is a prime number")   
  

