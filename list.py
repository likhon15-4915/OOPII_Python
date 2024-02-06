list = []  # emptylist

list.append("n1")
list.append("n2")
print(list)

list.append("n3")
print(list)

list.insert(1, "n4")
print(list)

list.index("n4")  # find out index number
print(list.index("n4"))

list.pop(1)  # delete index 1
print(list)

list.reverse()
print(list)
list.reverse()
print(list)
# insert
list.insert(1, "n4")
list.insert(1, "n7")
list.insert(1, "n5")
list.insert(1, "n6")
print(list)
# sorting
list.sort()
print(list)
# extend
list1 = ["n10", "n11", "n12"]
list.extend(list1)
print(list)

list.copy()
print(list)

list.remove("n12")
print(list)

list.count("n4")
print(list.count("n4"))

list.clear()
print(list)

student_name = ["Likhon", "Taohyd", "Ain"]
student_inf0 = [101, 102, 103, student_name]
print(student_inf0)

student_info2 = student_inf0.copy()
print("student info2", student_info2)

#user input in list
name=input("Your name")
student_name.append(name)
print(student_name)
student_inf0 = [101, 102, 103,104, student_name]
print(student_inf0)

name=input("Your name")
student_name.append(name)
print(student_name)

#Multiple input in list

list = []
n = int(input())
for i in range(n):
    a = input()
    list.append(a)
print(list)
