decimal = 13
def decimal2binary(decimal):
    if decimal > 1:
        decimal2binary(decimal //2)
    print(decimal % 2 , end="")

print("The Binary value of the decimal number",decimal,"is : ",end='')

decimal2binary(decimal)