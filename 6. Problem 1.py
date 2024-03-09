"""Take a string line as input from user. split that string based on white space
and convert each splitted substring in uppercase"""

String1=input()
print(String1)

n=[new.upper() for new in String1.split()]
print(n)

