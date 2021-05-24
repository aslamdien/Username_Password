# Selection Sort Exercise
# Give a list of numbers
numbers = [42, 12, 13, 89, 63, 11]


# Defining the numbers
def selection_sort(numbers):

    # giving the length of the numbers the variable name n
    n = len(numbers)

    # to look for the smallest number in range of the list say length of the numbers (n) -1
    for smallest in range(n-1):

        # giving the smallest number a variable of sn
        sn = smallest

        # to look for each position in the list
        for i in range(smallest+1, n):

            # this is the smallest number
            if numbers[i] < numbers[sn]:

                # position of the number
                sn = i

        # smallest will move to the left and biggest number will move to the right
        numbers[smallest], numbers[sn] = numbers[sn], numbers[smallest]


    # complete the function
    return numbers

# display the function
print(selection_sort(numbers))
