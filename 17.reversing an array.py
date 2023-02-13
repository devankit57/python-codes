import array as arr

#method 1

main=arr.array('i',[11,22,33,44,55])

print("Before reversal array is :",main)

main.reverse()

print("After reversal array is :",main)

#method 2

res_arr=arr.array('i',reversed(main))

print("After reversal array is :",res_arr)

#method 3

rever=res_arr[::-1]
print("Resultant Reversed array :",rever)

