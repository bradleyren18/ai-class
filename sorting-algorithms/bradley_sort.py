def merge(left, right):
    """
    Merge function from mergesort - combines two sorted lists into one sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def bradley_sort(arr):
    """
    Sorting algorithm that:
    1. Sorts every pair of elements
    2. Merges pairs of pairs using merge()
    3. Merges pairs of quadruples using merge()
    4. Continues until sorted
    5. Ignores leftovers that can't form pairs
    """
    if len(arr) <= 1:
        print(f"Array has {len(arr)} element(s), returning as-is: {arr}")
        return arr
    
    # Work on a copy to avoid modifying the original
    current = arr.copy()
    
    print(f"\n🔄 STARTING PAIR-MERGE SORT")
    print(f"📋 Original array: {current}")
    print(f"📏 Array length: {len(current)}")
    
    # Step 1: Sort every pair of elements
    print(f"\n📍 STEP 1: Sorting individual pairs")
    pairs_sorted = 0
    
    for i in range(0, len(current) - 1, 2):
        original_pair = [current[i], current[i + 1]]
        if current[i] > current[i + 1]:
            current[i], current[i + 1] = current[i + 1], current[i]
            print(f"  • Pair {i//2 + 1}: {original_pair} -> [{current[i]}, {current[i + 1]}] (swapped)")
        else:
            print(f"  • Pair {i//2 + 1}: {original_pair} -> [{current[i]}, {current[i + 1]}] (already sorted)")
        pairs_sorted += 1
    
    # Handle leftover element
    if len(current) % 2 == 1:
        print(f"  • Leftover element: {current[-1]} (no pair to sort with)")
    
    print(f"✅ Sorted {pairs_sorted} pairs")
    print(f"📋 After sorting pairs: {current}")
    
    # Step 2+: Merge pairs of groups of increasing size
    group_size = 2
    step_number = 2
    
    while group_size < len(current):
        # Check if we can actually perform any merges at this level
        pairs_available = len(current) // (group_size * 2)
        if pairs_available == 0:
            print(f"\n⏹️  No pairs of {group_size}-element groups available to merge")
            print(f"📋 Final result: {current}")
            break
        print(f"\n📍 STEP {step_number}: Merging pairs of {group_size}-element groups")
        new_current = []
        merges_performed = 0
        
        # Process pairs of groups (ignore leftover groups)
        for i in range(0, len(current) - group_size, group_size * 2):
            left_group = current[i:i + group_size]
            right_group = current[i + group_size:i + group_size * 2]
            merged = merge(left_group, right_group)
            new_current.extend(merged)
            merges_performed += 1
            print(f"  • Merge {merges_performed}: {left_group} + {right_group} = {merged}")
        
        # Add any leftover groups that couldn't form pairs
        remaining_start = (len(current) // (group_size * 2)) * (group_size * 2)
        if remaining_start < len(current):
            leftover = current[remaining_start:]
            new_current.extend(leftover)
            if len(leftover) == group_size:
                print(f"  • Single {group_size}-group leftover: {leftover} (no pair to merge with)")
            else:
                print(f"  • Partial leftover: {leftover} (no pair to merge with)")
        
        current = new_current
        print(f"✅ Performed {merges_performed} merges")
        print(f"📋 After merging {group_size}-element groups: {current}")
        
        group_size *= 2
        step_number += 1
    
    print(f"\n🎉 SORTING COMPLETE!")
    print(f"📋 Final result: {current}")
    return current


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [9, 18, 20, 14, 6, 23, 19, 78, 4, 26, 20, 22]
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n{'='*50}")
        print(f"Test {i}: {arr}")
        print(f"{'='*50}")
        
        result = bradley_sort(arr)
        print(f"\nFinal result: {result}")
        print(f"Is sorted: {result == sorted(arr)}")
        print(f"Original: {arr}")  # Show original is unchanged