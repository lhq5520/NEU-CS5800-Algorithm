import heapq
import math

# Problem 2 Hybrid Sort

# a)
# quick sort


def quick_sort(arr, low=0, high=None, depth=0):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, depth + 1)
        quick_sort(arr, pivot_index + 1, high, depth + 1)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# insersion sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift larger elements right
            j -= 1

        arr[j + 1] = key

# Heap Sort 


def heap_sort(arr):
    heapq.heapify(arr)  # Convert to heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    arr[:] = sorted_arr  # Update the original array in place

# Hybrid Sort


def hybrid_sort(arr):
    n = len(arr)

    if n > 0:
        max_depth = 2 * math.log2(n)
    else:
        max_depth = 0

    if n <= 16:
        print("using insertion sort")
        insertion_sort(arr)
    elif max_depth < 2 * math.log2(n):
        print("using quick sort")
        quick_sort(arr)
    else:
        print("using heap sort")
        heap_sort(arr)


if __name__ == "__main__":
    arr = [9, 3, 7, 1, 8, 5, 2, 4, 6, 0, 12, 11, 10, 13, 14, 15, 12]
    print("Before Sorting:", arr)
    hybrid_sort(arr)
    print("After Sorting:", arr)

