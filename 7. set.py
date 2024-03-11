"""built in function in Set
all()
any()
len()
max()
min()
sorted()
sum()
enumerate()"""

numbers={3,1,5,9}
numbers.add(7)
print(numbers)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
y=enumerate(numbers)
print(list(y))
