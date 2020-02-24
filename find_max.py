import numpy as nm

arr=nm.array([12,3,2,44,99,43,10,0,20])
count=0
maximum=arr[0]

for item in arr:
    if arr[count]>maximum:
        maximum=arr[count]
    count+=1
print(arr)
print('Maximum =',maximum)    
print(arr.max())