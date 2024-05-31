
# Dechen Dorji
# BBI'A'
#03230041

#Reference
#https://stackoverflow.com/questions/63515307/python-extract-numbers-from-text-file-and-total
#https://www.sanfoundry.com/python-program-read-file-print-numbers/

# solution

# Initialize the variables to store the first and last digit found in the string 
# go through the  each of character in the input string
def extract_digits(line):
    first_digit = None
    last_digit = None

# Will run through every character from the start by checking  if the current character is a digit

    for char in line:
        if char.isdigit():
            first_digit = char
            break
# Will run through every character from the end by checking  if the current character is a digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break

# Check if both 'first_digit' and 'last_digit' are found
#Combine 'first_digit' and 'last_digit' to form a two-digit number and convert it to an integer    
    if first_digit is not None and last_digit is not None:
            two_digit_number = int(first_digit + last_digit)
            return two_digit_number
    return 0


def calculate_sum(input_lines):
# Initialize a variable to store the cumulative sum
    total_sum = 0
# Iterate through the each line in the list of input lines    
    for line in input_lines:
        two_number = extract_digits(line)
        total_sum += two_number       
    return total_sum

# Entry point for script execution
if __name__ == "__main__":
    
    input_file = "041.txt"  

# Read the lines from the file
    with open(input_file, "r") as file:
        input_lines = file.readlines()
    
# Calculate the sum of the two-digit numbers
    result = calculate_sum(input_lines)
    print("The total sum of the given file ",input_file,'is' ,result)