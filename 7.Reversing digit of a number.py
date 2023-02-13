a=1234
reverse=0
while a>0:
    c=(a%10)
    a=(a//10)
    reverse=(reverse*10)+c

print(reverse)  