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
                print(f"Line {line_number}: Found mul({x},{y}) => {x} * {y} = {product}")

print(f"Total sum of all valid mul(X,Y): {total_sum}")

