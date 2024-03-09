# Sample Input
strings = ['hello', 'world', 'python', 'programming']

# Reverse each string in the list
for i in range(len(strings)):
    strings[i] = strings[i][::-1]

# Print the reversed strings
print("Reversed strings:")
for string in strings:
  print(string)