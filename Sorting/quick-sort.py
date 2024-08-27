def swap(arr, index_1, index_2):
    arr[index_1] , arr[index_2] = arr[index_2], arr[index_1]

def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)

    swap(arr, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(arr, left, right):
    if left < right:    
        pivot_index = pivot(arr, left, right)
        left = quick_sort_helper(arr, left, pivot_index - 1)
        right = quick_sort_helper(arr, pivot_index + 1, right)
    return arr

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)


arr = [4,6,1,7,3,2,5]
quick_sort(arr)
print(arr)