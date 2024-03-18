list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list=[]
for i in range(0,len(list1)):
    list.append(list1[i]* list2[i])
print(list)
