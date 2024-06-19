# 1. Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating the sum
sum = num1 + num2

# Printing the sum
print(f"The sum of {num1} and {num2} is: {sum}")


# 2. Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage:
number = int(input("Enter a number: "))
check_even_odd(number)

# 3. calculates the factorial of a given number
def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial 
# Taking input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial using iterative method
factorial_iter = factorial_iterative(num)
print(f'Factorial of {num} : {factorial_iter}')

# 4. asks the user for their name and then prints a greeting message.
# Ask the user for their name
name = input("What is your name? ")

# Print a greeting message
print(f"Hello, {name}! Nice to meet you.")

# 5. string input from the user and writes it to a text file.

def main():
    # Take input from the user
    user_input = input("Enter a string: ")
    
    # Specify the file name
    file_name = "user_input.txt"
    
    # Write the input to a text file
    try:
        with open(file_name, 'w') as file:
            file.write(user_input)
        print(f"Successfully wrote the input to {file_name}")
    except IOError:
        print(f"Error writing to {file_name}")

if __name__ == "__main__":
    main()

# 6. Program that reads the content of a text file and prints it to the console:

file_path = 'sample.txt'
 
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()
         
        # Print the content
        print("File Content:\n", file_content)
 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 7. Program that takes a string as input and returns its length:
def calculate_string_length(input_string):
    return len(input_string)

string = input("Enter a string: ")
print(f"The length of the string '{string}' is: {calculate_string_length(string)}")


# 8. Program that concatenates two strings and returns the result:
def concatenate_strings(str1, str2):
    return str1 + str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print(f"The concatenated string is: {concatenate_strings(string1, string2)}")


# 9. Program that checks if a substring is present in a given string:
def check_substring(main_string, sub_string):
    return sub_string in main_string

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")
if check_substring(main_str, sub_str):
    print(f"'{sub_str}' is present in '{main_str}'.")
else:
    print(f"'{sub_str}' is not present in '{main_str}'.")

# 10. Program that converts a given string to uppercase:
def convert_to_uppercase(input_string):
    return input_string.upper()

string = input("Enter a string to convert to uppercase: ")
print(f"The uppercase version of '{string}' is: {convert_to_uppercase(string)}")


# 11. Program that generates the first n numbers in the Fibonacci sequence:
def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = generate_fibonacci(num)
print(f"The first {num} numbers in the Fibonacci sequence are: {fib_numbers}")


# 12. Program that calculates the sum of the digits of a given number:
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

num = int(input("Enter a number to calculate the sum of its digits: "))
print(f"The sum of digits of {num} is: {sum_of_digits(num)}")


# 13. Program that asks the user for their birth year and calculates their age:
from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

year = int(input("Enter your birth year: "))
age = calculate_age(year)
print(f"You are {age} years old.")


# 14. Program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines:
def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (leave empty to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

lines = read_lines_until_empty()
print("Lines entered:")
for line in lines:
    print(line)

# 15. Program that reads data from a CSV file and prints it to the console:
import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
if __name__ == "__main__":
    csv_filename = 'data.csv'  # Replace with your CSV file name
    read_csv_file(csv_filename)




# 16. Program that counts the frequency of each character in a string:

from collections import Counter

def count_character_frequency(input_string):
    return Counter(input_string)

string = input("Enter a string to count character frequencies: ")
frequency = count_character_frequency(string)
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

# 17. Program that converts a given string to title case (first letter of each word capitalized):
def convert_to_title_case(input_string):
    return input_string.title()

string = input("Enter a string to convert to title case: ")
print(f"The title cased version of '{string}' is: {convert_to_title_case(string)}")


# 18. Program that checks if two strings are anagrams of each other:
def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if check_anagram(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")


# 19. Program that removes all punctuation from a given string:
import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use translate method to remove punctuation
    return input_string.translate(translator)

# Example usage:
if __name__ == "__main__":
    input_string = "Hello! This, is a sample text; with punctuation."
    result_string = remove_punctuation(input_string)
    print("Original string:", input_string)
    print("String without punctuation:", result_string)
 


# 20. Program that takes a list of numbers and returns their sum:
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    # Prompt user for input
    input_str = input("Enter numbers separated by spaces: ")
    
    # Split input string into a list of strings
    numbers_str = input_str.split()
    
    # Convert list of strings to list of integers
    numbers = list(map(int, numbers_str))
    
    # Calculate sum using the function
    total_sum = calculate_sum(numbers)
    
    # Print the result
    print(f"The sum of numbers {numbers} is: {total_sum}")



# 21. Program that counts the occurrences of a specific element in a list:
def count_occurrences(input_list, element):
    return input_list.count(element)

# Example usage:
my_list = [1, 2, 3, 4, 2, 2, 5, 6, 2]
element_to_count = 2
print(f"The element {element_to_count} appears {count_occurrences(my_list, element_to_count)} times in the list.")


# 22. Program that returns the minimum and maximum values in a list of numbers:
def find_min_max(input_list):
    if len(input_list) == 0:
        return None, None
    min_val = min(input_list)
    max_val = max(input_list)
    return min_val, max_val

# Example usage:
numbers = [3, 1, 7, 2, 8, 4, 5]
min_value, max_value = find_min_max(numbers)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")


# 23. Program that converts temperature from Celsius to Fahrenheit and vice versa based on user input:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Enter '1' to convert Celsius to Fahrenheit, '2' to convert Fahrenheit to Celsius: ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius.")
else:
    print("Invalid choice.")


# 24. Program that acts as a simple calculator:

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator!"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /): ")
result = calculator(num1, num2, op)
print(f"{num1} {op} {num2} = {result}")

# 25. Program that copies the contents of one text file to another:
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Contents of {source_file} copied to {destination_file} successfully.")
    except FileNotFoundError:
        print("File not found!")

# Example usage:
source = 'source.txt'
destination = 'destination.txt'
copy_file(source, destination)


# 26. Program that checks if a string starts with a given prefix or ends with a given suffix:
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")
starts_with, ends_with = check_prefix_suffix(string, prefix, suffix)
print(f"The string '{string}' starts with '{prefix}': {starts_with}")
print(f"The string '{string}' ends with '{suffix}': {ends_with}")


# 27. Program that converts a string into a list of its characters:
def string_to_list(input_string):
    return list(input_string)

string = input("Enter a string: ")
char_list = string_to_list(string)
print(f"The characters of '{string}' as a list are: {char_list}")









