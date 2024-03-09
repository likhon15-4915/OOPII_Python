"""
You should take a string of 'm' size without any space. Where m>=8.
Now, Replace first '3' characters at that string '3' digits,
replace the last '3' character by special character
and rest at the character should be uppercase.
sapmle input: Programming
sample output: 321GRAMM#!@
"""

def transform(input_string):
    if len(input_string) < 8:
        return "Input string length should be at least 8 characters."

    # Replace first 3 characters with digits
    transformed = input_string[:3].replace(input_string[:3], '321')

    # Replace last 3 characters with a special character
    transformed += input_string[-4:-1].replace(input_string[-4:-1], '!@#')

    # Convert remaining characters to uppercase
    transformed += input_string[3:-4].upper()

    return transformed


# Example usage
input_str = "Programming"
output_str = transform(input_str)
print("Input:", input_str)
print("Output:", output_str)
def transform(input_string):
    if len(input_string) < 8:
        return "Input string length should be at least 8 characters."

    # Replace first 3 characters with digits
    transformed = input_string[:3].replace(input_string[:3], '321')

    # Replace last 3 characters with a special character
    transformed += input_string[-4:-1].replace(input_string[-4:-1], '!@#')

    # Convert remaining characters to uppercase
    transformed += input_string[3:-4].upper()

    return transformed


# Example usage
input_str = "Programming"
output_str = transform(input_str)
print("Input:", input_str)
print("Output:", output_str)
