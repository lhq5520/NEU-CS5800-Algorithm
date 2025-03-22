arr = [1, 3, 2, 5, 4, 6, 8 , 10, 15]


def new_sort(arr, p, r):
    if arr[p] > arr[r]:
        arr[p], arr[r] = arr[r], arr[p]
    if p + 1 < r:
        k = (r - p + 1) // 3
        new_sort(arr, p, r - k)
        new_sort(arr, p + k, r)
        new_sort(arr, p, r - k)
    return arr

print("Before sorting: ", arr)
print("After sorting: ", new_sort(arr, 0, len(arr) - 1))