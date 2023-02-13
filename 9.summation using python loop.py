numbers=[1,2,3,4,5]
total=0

for number in numbers:
    total=total+number
print(total)

#Method 2

length=len(numbers)
sum1=0
for i in range(1,length+1):
    sum1=sum1+i
print(sum1)

#Method 3

def sum_numbers(numbers):
    tot=0
    for number in numbers:
        tot+=number

    return tot
print(sum_numbers([1,2,3,4,5]))


print(sum([1,2,3,4,5]))
print(sum((1,2,3,4,5)))