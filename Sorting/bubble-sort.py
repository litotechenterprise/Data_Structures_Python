
def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1] , my_list[j]

    return my_list


def bubbleSort(arr):
    n = len(arr)

    # Going through all array elements
    for i in range(0,n-1):
        # Go through all array elements, minus already sorted
        for j in range(0,n-i-1):
            # Swap if number is greater than the next
            if arr[j] > arr[j+1]:
                arr[j], arr[j+ 1] = arr[j+1], arr[j]