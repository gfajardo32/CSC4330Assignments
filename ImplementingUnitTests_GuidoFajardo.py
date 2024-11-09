#Implementing unit tests for sorting algorithms
#Guido Fajardo


import unittest
import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        merged = []
        i = j = 0

        # Merge the two arrays while comparing their elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append any remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    return merge(left_part, right_part)

class TestMergeSort(unittest.TestCase):
    def test_positive_case(self):
        """Positive Case: Test sorting of a typical unsorted array."""
        arr = [34, 7, 23, 32, 5, 62]
        expected = sorted(arr)
        result = merge_sort(arr)
        self.assertEqual(result, expected)

    def test_negative_case(self):
        """Negative Case: Verify handling of invalid input types."""
        arr = [10, 'twenty', 30, None, 50]
        with self.assertRaises(TypeError):
            merge_sort(arr)

    def test_performance_case(self):
        """Performance Case: Test efficiency with a large array."""
        arr = random.sample(range(1000000), 100000)  # Large array with 100,000 elements
        start_time = time.time()
        result = merge_sort(arr)
        end_time = time.time()
        expected = sorted(arr)
        self.assertEqual(result, expected)
        self.assertTrue((end_time - start_time) < 10)  # The sort should complete within 10 seconds

    def test_boundary_case(self):
        """Boundary Case: Test sorting of edge cases."""
        # Empty array
        self.assertEqual(merge_sort([]), [])

        # Single-element array
        self.assertEqual(merge_sort([42]), [42])

        # Array with duplicate values
        arr_duplicates = [5, 1, 3, 5, 2, 1]
        expected_duplicates = sorted(arr_duplicates)
        self.assertEqual(merge_sort(arr_duplicates), expected_duplicates)

        # Already sorted array
        arr_sorted = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr_sorted), arr_sorted)

        # Reverse-sorted array
        arr_reverse = [5, 4, 3, 2, 1]
        expected_reverse = sorted(arr_reverse)
        self.assertEqual(merge_sort(arr_reverse), expected_reverse)

    def test_idempotency_case(self):
        """Idempotency Case: Confirm consistent results across multiple runs."""
        arr = random.sample(range(1000), 100)
        first_sort = merge_sort(arr)
        second_sort = merge_sort(first_sort)
        self.assertEqual(first_sort, second_sort)
        self.assertEqual(first_sort, sorted(arr))

if __name__ == '__main__':
    unittest.main()
