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

    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")

    nums = [int(n) for n in numbers.split(",") if n]

    return sum(nums)