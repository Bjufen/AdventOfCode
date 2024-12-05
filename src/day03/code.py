import re


file_path = "../../resources/day03.txt"

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total_sum = 0

with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        matches = re.findall(mul_pattern, line)
        if matches:
            for x, y in matches:
                product = int(x) * int(y)
                total_sum += product

print(f"Total sum of all valid mul(X,Y) (Part 1): {total_sum}")


def process_input(input_str):
    mul_enabled = True  # Initial state: mul instructions are enabled
    total_sum = 0
    line_number = 1

    # Compile regular expressions for efficiency
    mul_pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    do_pattern = re.compile(r'do\(\s*\)')
    dont_pattern = re.compile(r'don\'t\(\s*\)')

    # Process line by line for line number tracking
    for line in input_str.splitlines():
        index = 0
        length = len(line)

        while index < length:
            # Try to match each pattern at the current index
            mul_match = mul_pattern.match(line, index)
            do_match = do_pattern.match(line, index)
            dont_match = dont_pattern.match(line, index)

            if do_match:
                # Enable mul instructions
                mul_enabled = True
                index = do_match.end()
            elif dont_match:
                # Disable mul instructions
                mul_enabled = False
                index = dont_match.end()
            elif mul_match:
                if mul_enabled:
                    # Extract numbers and add their product to the total sum
                    x = int(mul_match.group(1))
                    y = int(mul_match.group(2))
                    product = x * y
                    total_sum += product
                index = mul_match.end()
            else:
                # Move to the next character if no pattern matches
                index += 1

        line_number += 1

    return total_sum

# Read the input from 'day03.txt'
file_path = "../../resources/day03.txt"

with open(file_path, 'r') as file:
    input_str = file.read()

# Process the input and print the result
total_sum = process_input(input_str)
print(f"Total sum of all valid mul(X,Y) (Part 2): {total_sum}")
