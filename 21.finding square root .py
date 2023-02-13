#Three Method

#Method 1.Using ** exponent
#Method 2 Using math.sqrt()
#Method 3 Using math.pow()

num=int(input("Enter a number : "))

sq=num**0.5

print("SQRT IS ",sq)



#<----------------Method 2---------------------->

import math

sq1=math.sqrt(num)
sq2=math.pow(num,0.5)  #Method 3

print("SQRT by method 2 ",sq1)
print("SQRT by method 3 ",sq2)

