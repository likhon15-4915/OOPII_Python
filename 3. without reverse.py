"""list=[5,2,3,4,1]
a=[]
for item in reversed(list):
    a.append(item)
print(a)

"""
list=[5,2,3,4,1]
length=len(list)
for i in range(length-1,-1,-1):
    print(list[i])
