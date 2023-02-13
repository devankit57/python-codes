import array as arr
alpha=arr.array('i',[25,11,7,75,560])
length=len(alpha)
max_element=alpha[0]

for i in range(1,length):
    if (max_element<alpha[i]):
        
        max_element=alpha[i]

print("The largest element is ",max_element)
