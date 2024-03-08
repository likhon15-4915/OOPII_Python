#2D list
Two_D= [[1,2,4,6],[3,7,8,10]]
"""print(Two_D[1][2])
print(Two_D[0][3])"""

sum=0
for i in Two_D:
    for j in i:
        sum= sum+j
print(sum)

mul=1
for i in Two_D:
    for j in i:
        mul=mul*j
print(mul)