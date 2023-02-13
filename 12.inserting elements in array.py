import array as arr
balance=arr.array('i',[300,200,100])

length=len(balance)
balance.insert(length,150)
print(balance)
