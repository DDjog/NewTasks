numbers = [6,4,2,1,3,2,1,6]
# print(numbers.sort())
# print(numbers)


def sorting_numbers(numbers):
    """
            Sorting list of numbers

            Parameters
            ----------
            numbers: integer
               the list of numbers

            Returns
            -------
            numbers: integer
                the sorted list of numbers

            Examples
            --------
            Sorting list of numbers
            rslt=sorting_numbers(6,4,2,1,3,2,1,6)
            print(rslt)
            (1,1,2,2,3,4,6,6)
            """
    n = len(numbers)
    for i in range(n):
        for j in range (0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


sorting_numbers(numbers)
print(numbers)

