numbers1 = [6,4,2,1,3,2,1,6]
numbers2 = (6,4,2,1,3,2,1,6)
# print(numbers.sort())
# print(numbers)


def sort_list_of_numbers(numbers1):
    """
            Sorting list of numbers

            Parameters
            ----------
            numbers1: integers
               the list of numbers

            Returns
            -------
            list of integers
                the sorted list of numbers

            Examples
            --------
            Sorting list of numbers1
            numbers1 = [6,4,2,1,3,2,1,6]
            rslt=sort_list_of_numbers(numbers1)
            print(rslt)
            [1,1,2,2,3,4,6,6]
            """
    n = len(numbers1)
    for i in range(n):
        for j in range (0, n-i-1):
            if numbers1[j] > numbers1[j+1]:
                numbers1[j], numbers1[j+1] = numbers1[j+1], numbers1[j]
    print("Sorted list of numbers")
    return(numbers1)


def check_and_sort_numbers(*args):
    """
               Checking and sorting numbers

               Parameters
               ----------
               args: integers
                  the changeable number of numbers

               Returns
               -------
               list of integers
                   the sorted list of numbers

               Examples
               --------
               Sorting number of numbers
               args = (6,4,2,1,3,2,1,6)
               rslt=check_and_sort_numbers(args)
               print(rslt)
               [1,1,2,2,3,4,6,6]
               """
    n = len(args)
    numbers2 = list(args)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers2[j] > numbers2[j + 1]:
                numbers2[j], numbers2[j + 1] = numbers2[j + 1], numbers2[j]
    print("Number of arguments: ", n)
    print("Sorted numbers")
    return numbers2


sorted_list_of_numbers = sort_list_of_numbers(numbers1)
print(sorted_list_of_numbers)
print("-------------------------------")
sorted_numbers = check_and_sort_numbers(*numbers2)
print(sorted_numbers)

