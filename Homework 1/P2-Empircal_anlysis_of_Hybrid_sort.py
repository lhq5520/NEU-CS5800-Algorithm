import heapq
import math
import numpy as np
import time
import matplotlib.pyplot as plt

# Quick Sort
def quick_sort(arr, low=0, high=None, depth=0):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"[Quick Sort] Depth {depth}: Pivot at index {pivot_index} with value {arr[pivot_index]}")
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

# Insertion Sort
def insertion_sort(arr):
    print("[Insertion Sort] Starting sort...")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("[Insertion Sort] Completed.")

# Heap Sort
def heap_sort(arr):
    print("[Heap Sort] Starting sort...")
    arr = list(arr)  # Convert to list to fix the TypeError
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    arr[:] = sorted_arr
    print("[Heap Sort] Completed.")

# Hybrid Sort
def hybrid_sort(arr):
    n = len(arr)
    if n > 0:
        max_depth = 2 * math.log2(n)
    else:
        max_depth = 0

    if n <= 16:
        print("[Hybrid Sort] Using Insertion Sort.")
        insertion_sort(arr)
    elif max_depth < 2 * math.log2(n):
        print("[Hybrid Sort] Using Quick Sort.")
        quick_sort(arr)
    else:
        print("[Hybrid Sort] Using Heap Sort.")
        heap_sort(arr)

# Generate datasets
sizes = [1000, 10000, 100000, 500000]
results = {"Insertion Sort": [], "Quicksort": [], "Heapsort": [], "Hybrid Sort": []}

def measure_time(sort_func, data):
    arr_copy = data.copy()
    print(f"[Measure] Running {sort_func.__name__} on dataset of size {len(data)}...")
    start_time = time.time()
    sort_func(arr_copy)
    elapsed_time = time.time() - start_time
    print(f"[Measure] {sort_func.__name__} completed in {elapsed_time:.4f} seconds.")
    return elapsed_time

for size in sizes:
    datasets = {
        'Random': np.random.randint(0, size, size),
        'Nearly Sorted': np.sort(np.random.randint(0, size, size))[:int(size*0.9)].tolist() + np.random.randint(0, size, int(size*0.1)).tolist(),
        'Reverse Sorted': np.sort(np.random.randint(0, size, size))[::-1]
    }

    for data_type, data in datasets.items():
        print(f"\n[Dataset] Testing on {data_type} data of size {size}...")
        results["Insertion Sort"].append(measure_time(insertion_sort, data))
        results["Quicksort"].append(measure_time(quick_sort, data))
        results["Heapsort"].append(measure_time(heap_sort, data))
        results["Hybrid Sort"].append(measure_time(hybrid_sort, data))

# Plotting results
for algorithm, times in results.items():
    plt.plot(sizes * 3, times, label=algorithm)
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()
