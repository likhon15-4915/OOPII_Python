"""
1. upper()
2. lower()
3. replace()
4. find()
5. rstrip()
6. split()
7. Startswith()
8. index()             """

String1="Welcome to Python"
String2="Welcome to Python Programming, Let's Explore it, and filfill your goal."

#sting split: split()
print(String1.split())
print(String2.split(","))

print(String1.upper())
print(String1.lower())
print(String1.index("P"))

#replace
r= String1.replace("Welcome","Hello")
print(r)

#find
x=String2.find("Welcome")
print(x)

#rstrip()
String3="Its String no.3!"
y=String3.rstrip("!")
print(y)
y=String3.rstrip("3!")
print(y)

#Startswith()
print(String1.startswith("Welcome"))

