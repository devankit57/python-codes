import array as arr

def findkmax(k,array):
    array.sort(reverse=True)
    print("Kth maximum element is : ",array[k-1])



def findkmin(k,array):
    array.sort()
    print("Kth min element is : ",array[k-1])

array=arr.array('i',[1,7,6,8,9,2,4,5,3,0])

findkmin(1,array)
findkmax(1,array)