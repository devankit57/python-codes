import array as arr
#method 1
main=arr.array('i',[1,2,2,2,2,2,3,3,3,5,5])
length=len(main)
new_arr=arr.array('i',[])
for i in range(0,length):
    if main[i] not in new_arr:
        new_arr.append(main[i])


print(new_arr)

#method 2

def removeDuplicates(ar,n):
    if n==0 or n==1:
        return n
    temp =list(range(n))
    j=0
    for i in range(0,n-1):
        if ar[i]!=ar[i+1]:
            temp[j]=ar[i]
            j+=1
    temp[j]=ar[n-1]
    j+=1
    for i in range(0,j):
        ar[i]=temp[i]
    return j

ar=arr.array('i',[1,2,2,3,4,4,4,5,5])
n=len(ar)
n=removeDuplicates(ar,n)
for i in range(n):
    print("%d"%(ar[i]),end=" ")
