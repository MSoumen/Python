import numpy as nm

arr1=nm.array([1,2,3,4,5])
arr2=nm.array([5,4,3,2,1])
count=0
for item in arr2:
    #print(item)
    count+=1

arr3=nm.array([None]*count)     # This create an empty array of size=count--------

for i in range(count):
    arr3[i]=arr2[i]+arr1[i]

print(arr1)   
print(arr2)
print(arr3)
