n=[1,2,3,4,5]
#squared_value=[1,4,9,16]

"""newlist = []
for i in n:
    newlist.append(i**2)
print(newlist)"""


"""squared_value = []
for x in range(len(n)):
    x=n[x]**2
    squared_value.append(x)
print(squared_value)"""

                    #list_comprehension
#syntax---
#newlist=[expression(element)for element in oldlist if condition]

squared_value=[n[x]**2 for x in range(len(n)) if (x %2 != 0)]
print(squared_value)
