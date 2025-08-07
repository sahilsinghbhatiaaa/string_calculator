'''
TDD:
Failing test first
Writing that make test pass
Refactor to improve it
'''

def add(numbers):
    if not numbers:
        return 0

    delimiters = [",", "\n", " "]

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delimiter = parts[0][2:]
        numbers = parts[1]
        delimiters = [custom_delimiter]

    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")

    nums = [int(n) for n in numbers.split(",") if n]

    return sum(nums)