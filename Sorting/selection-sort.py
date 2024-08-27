
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr) -1):
        # Find min in sorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
             # Swap the elements
            arr[i], arr[min_index] = arr[min_index], arr[i]    
    return arr



arr = [4,7,12,2,5,3]
print(selection_sort(arr))