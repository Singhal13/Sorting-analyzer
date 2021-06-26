def bubble_sort(arr):
    swap_status = True
    for j in range(len(arr)-1, 0, -1):
        if swap_status == False:
            break
        swap_status = False
        for i in range(0, j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_status = True
    return arr

def merge_sorted(arr1, arr2):
    sorted_arr = []
    i , j = 0 , 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    if i < len(arr1):
        sorted_arr += arr1[i:]

    if j < len(arr2):
        sorted_arr += arr2[j:]

    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort((arr[middle:]))
        return merge_sorted(l1, l2)

def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller , equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

print("All Algorithms Loaded")