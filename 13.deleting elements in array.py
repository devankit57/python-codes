import array as arr
a=arr.array('b',[2,3,4,5,6])

x=a.index(3)
print(x)
a.insert(5,3)
x=a.index(3)
print(x)
#a.pop(x)

print(a)
