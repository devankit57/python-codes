#numpy.partition() function

import numpy as test

in_arr=test.array([2,0,1,5,4,9])

print("Input array :",in_arr)
out_arr=test.partition(in_arr,2)
print("Output partitioned array :",out_arr)