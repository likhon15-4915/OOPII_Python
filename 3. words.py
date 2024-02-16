Words=["Pen","Pencil","Projector"]
b=[]
for item in Words:
    b=""
    for b in item:
        res=b.split()
        print(res,end="")

        c = [b]

print(c)
"""c=list(b)
item_lengths = [len(item) for item in c]
print(item_lengths)

for item in b:
    print(item.upper())  # Convert to uppercase
    #print(item.lower())  # Convert to lowercase"""
