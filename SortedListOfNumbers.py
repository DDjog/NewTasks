numbers = [6,4,2,1,3,2,1,6]
# print(numbers.sort())
# print(numbers)


def sorting_numbers(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range (0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


sorting_numbers(numbers)
print(numbers)

