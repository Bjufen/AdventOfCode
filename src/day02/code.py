collection = []

file_path = '../../resources/day02.txt'


def is_increasing(numbers):
    return all(x < y for x, y in zip(numbers, numbers[1:]))


def is_decreasing(numbers):
    return all(x > y for x, y in zip(numbers, numbers[1:]))


def is_valid_difference(numbers):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))


def determine_safety(numbers):
    return (is_increasing(numbers) or is_decreasing(numbers)) and is_valid_difference(numbers)


with open(file_path) as file:
    for line in file:
        report = list(map(int, line.split()))
        collection.append((report, determine_safety(report)))

print("Part 1 (Sum of safe reports)", sum(boolean for _, boolean in collection))


def can_be_safe_by_removing_one(numbers):
    for i in range(len(numbers)):
        modified_list = numbers[:i] + numbers[i+1:]
        if determine_safety(modified_list):
            return True
    return False


can_be_safe = [(numbers, can_be_safe_by_removing_one(numbers)) for numbers, _ in collection]

print("Part 2 (Sum of reports that can be made safe by removing one number)", sum(boolean for _, boolean in can_be_safe))

