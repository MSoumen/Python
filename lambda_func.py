#Create lambda func for make num^num
num_to_the_power_num=lambda a: a**a
print(num_to_the_power_num(4))

###Some operation on lambda
#filter():filtered out some items from a list for a given condition
numList=[12,13,23,24,55,11,7,2,98,77]
evenNum= list(filter(lambda num: num%2==0,numList))
oddNum=list(filter(lambda num:num%2!=0,numList))
print(evenNum)
print(oddNum)

#map(): apply some calculation on each items of the list and updated the list
updated_by_adding_2=list(map(lambda num:num+2,numList))
print(numList)
print(updated_by_adding_2)

#reduce():it shrink the whole list to a one value
from functools import reduce 
sum_of_all_items=int(reduce(lambda x,y:x+y,numList))
print(sum_of_all_items)
