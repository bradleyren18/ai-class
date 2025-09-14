import random
import copy

def calculate_score(arr, target):
    """Calculate how many elements are in their correct position."""
    return sum(1 for i in range(len(arr)) if arr[i] == target[i])

def insertion_sort(arr):
    """
    Insertion sort with step logging.
    Logs every shift operation.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            steps.append((arr.copy(), calculate_score(arr, target)))
            j -= 1
        
        # Insert the key
        if j + 1 != i:  # Only log if there was actually a change
            arr[j + 1] = key
            steps.append((arr.copy(), calculate_score(arr, target)))
    
    return steps

def selection_sort(arr):
    """
    Selection sort with step logging.
    Logs each comparison and swap.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    for i in range(len(arr)):
        min_idx = i
        
        # Find minimum element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                # Log after finding new minimum
                steps.append((arr.copy(), calculate_score(arr, target)))
        
        # Swap if needed
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append((arr.copy(), calculate_score(arr, target)))
    
    return steps

def bubble_sort(arr):
    """
    Bubble sort with step logging.
    Logs every swap.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append((arr.copy(), calculate_score(arr, target)))
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return steps

def bogosort(arr):
    """
    Bogosort with step logging.
    Logs every shuffle attempt. Capped at 1000 iterations.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    iterations = 0
    while arr != target and iterations < 1000:
        random.shuffle(arr)
        steps.append((arr.copy(), calculate_score(arr, target)))
        iterations += 1
    
    return steps

def gnome_sort(arr):
    """
    Gnome sort with step logging.
    Logs every comparison and swap.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    pos = 0
    while pos < len(arr):
        # Log comparison
        steps.append((arr.copy(), calculate_score(arr, target)))
        
        if pos == 0 or arr[pos] >= arr[pos - 1]:
            pos += 1
        else:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            steps.append((arr.copy(), calculate_score(arr, target)))
            pos -= 1
    
    return steps

def merge_sort(arr):
    """
    Merge sort with step logging.
    Logs overwrites during merge operations.
    """
    if not arr:
        return []
    
    target = sorted(arr)
    steps = []
    result = arr.copy()
    
    # Log initial state
    steps.append((result.copy(), calculate_score(result, target)))
    
    def merge_sort_helper(arr, left, right, temp):
        if left >= right:
            return
        
        mid = (left + right) // 2
        merge_sort_helper(arr, left, mid, temp)
        merge_sort_helper(arr, mid + 1, right, temp)
        merge(arr, left, mid, right, temp)
    
    def merge(arr, left, mid, right, temp):
        i, j, k = left, mid + 1, left
        
        # Merge the two halves
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back to original array and log each overwrite
        for i in range(left, right + 1):
            if arr[i] != temp[i]:
                arr[i] = temp[i]
                steps.append((arr.copy(), calculate_score(arr, target)))
    
    temp = [0] * len(result)
    merge_sort_helper(result, 0, len(result) - 1, temp)
    
    return steps

def heap_sort(arr):
    """
    Heap sort with step logging.
    Logs swaps during heapify and main sorting.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append((arr.copy(), calculate_score(arr, target)))
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        steps.append((arr.copy(), calculate_score(arr, target)))
        heapify(arr, i, 0)
    
    return steps

def quicksort(arr):
    """
    Quicksort with step logging.
    Logs swaps during partitioning.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    target = sorted(arr)
    steps = []
    
    # Log initial state
    steps.append((arr.copy(), calculate_score(arr, target)))
    
    def quicksort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi - 1)
            quicksort_helper(arr, pi + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    steps.append((arr.copy(), calculate_score(arr, target)))
        
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            steps.append((arr.copy(), calculate_score(arr, target)))
        
        return i + 1
    
    quicksort_helper(arr, 0, len(arr) - 1)
    return steps

# Example usage and testing
# if __name__ == "__main__":
#     test_arrays = [
#         [64, 34, 25, 12, 22, 11, 90],
#         [5, 2, 4, 6, 1, 3],
#         [1],
#         [],
#         [3, 3, 3, 3],
#         [5, 4, 3, 2, 1]
#     ]
    
#     algorithms = {
#         "Insertion Sort": insertion_sort,
#         "Selection Sort": selection_sort,
#         "Bubble Sort": bubble_sort,
#         "Bogosort": bogosort,
#         "Gnome Sort": gnome_sort,
#         "Merge Sort": merge_sort,
#         "Heap Sort": heap_sort,
#         "Quicksort": quicksort
#     }
    
#     # Test with a small array
#     test_arr = [64, 34, 25, 12, 22]
#     print(f"Testing with array: {test_arr}")
#     print("-" * 50)
    
#     for name, func in algorithms.items():
#         print(f"\n{name}:")
#         try:
#             steps = func(test_arr)
#             print(f"Steps: {len(steps)}")
#             if steps:
#                 print(f"Initial: {steps[0][0]} (score: {steps[0][1]})")
#                 print(f"Final: {steps[-1][0]} (score: {steps[-1][1]})")
#             if name == "Bogosort" and len(steps) >= 1001:  # 1000 iterations + initial state
#                 print("(Capped at 1000 iterations)")
#         except Exception as e:
#             print(f"Error: {e}")