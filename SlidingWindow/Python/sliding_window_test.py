"""
Test class for the Sliding Window implementation.
This class provides methods to test various sliding window algorithms.
"""
from sliding_window_template import SlidingWindowTemplate
from sliding_window_solution import SlidingWindowSolution
from sliding_window import SlidingWindow

# Uncomment the line below to use your implementation
# SlidingWindow = SlidingWindowTemplate
# Comment the line below to use your implementation
SlidingWindow = SlidingWindow

def test_max_sum_subarray():
    """
    Test the maximum sum subarray algorithm.
    """
    print("\n=== Testing Maximum Sum Subarray ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular array
    arr1 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k1 = 4
    result1 = sw.max_sum_subarray(arr1, k1)
    expected1 = 39  # 10 + 23 + 3 + 3
    if result1 == expected1:
        print("PASS: Maximum sum subarray of size 4 is 39")
    else:
        print(f"FAIL: Expected 39, got {result1}")
    
    # Test case 2: Array with negative numbers
    arr2 = [-1, -2, -3, -4, -5]
    k2 = 3
    result2 = sw.max_sum_subarray(arr2, k2)
    expected2 = -6  # -1 + -2 + -3
    if result2 == expected2:
        print("PASS: Maximum sum subarray of size 3 is -6")
    else:
        print(f"FAIL: Expected -6, got {result2}")
    
    # Test case 3: Empty array
    arr3 = []
    k3 = 3
    result3 = sw.max_sum_subarray(arr3, k3)
    expected3 = 0
    if result3 == expected3:
        print("PASS: Maximum sum subarray of empty array is 0")
    else:
        print(f"FAIL: Expected 0, got {result3}")
    
    # Test case 4: k > array length
    arr4 = [1, 2, 3]
    k4 = 4
    result4 = sw.max_sum_subarray(arr4, k4)
    expected4 = 0
    if result4 == expected4:
        print("PASS: Maximum sum subarray with k > array length is 0")
    else:
        print(f"FAIL: Expected 0, got {result4}")

def test_min_size_subarray_sum():
    """
    Test the minimum size subarray sum algorithm.
    """
    print("\n=== Testing Minimum Size Subarray Sum ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular array
    arr1 = [2, 3, 1, 2, 4, 3]
    target1 = 7
    result1 = sw.min_size_subarray_sum(arr1, target1)
    expected1 = 2  # [4, 3]
    if result1 == expected1:
        print("PASS: Minimum size subarray with sum >= 7 is 2")
    else:
        print(f"FAIL: Expected 2, got {result1}")
    
    # Test case 2: No subarray with sum >= target
    arr2 = [1, 2, 3, 4, 5]
    target2 = 20
    result2 = sw.min_size_subarray_sum(arr2, target2)
    expected2 = 0
    if result2 == expected2:
        print("PASS: No subarray with sum >= 20")
    else:
        print(f"FAIL: Expected 0, got {result2}")
    
    # Test case 3: Empty array
    arr3 = []
    target3 = 5
    result3 = sw.min_size_subarray_sum(arr3, target3)
    expected3 = 0
    if result3 == expected3:
        print("PASS: Minimum size subarray of empty array is 0")
    else:
        print(f"FAIL: Expected 0, got {result3}")
    
    # Test case 4: Single element array
    arr4 = [10]
    target4 = 10
    result4 = sw.min_size_subarray_sum(arr4, target4)
    expected4 = 1
    if result4 == expected4:
        print("PASS: Minimum size subarray with sum >= 10 is 1")
    else:
        print(f"FAIL: Expected 1, got {result4}")

def test_longest_substring_without_repeating_chars():
    """
    Test the longest substring without repeating characters algorithm.
    """
    print("\n=== Testing Longest Substring Without Repeating Characters ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular string
    s1 = "abcabcbb"
    result1 = sw.longest_substring_without_repeating_chars(s1)
    expected1 = 3  # "abc"
    if result1 == expected1:
        print("PASS: Longest substring without repeating characters is 3")
    else:
        print(f"FAIL: Expected 3, got {result1}")
    
    # Test case 2: String with all same characters
    s2 = "bbbbb"
    result2 = sw.longest_substring_without_repeating_chars(s2)
    expected2 = 1  # "b"
    if result2 == expected2:
        print("PASS: Longest substring without repeating characters is 1")
    else:
        print(f"FAIL: Expected 1, got {result2}")
    
    # Test case 3: Empty string
    s3 = ""
    result3 = sw.longest_substring_without_repeating_chars(s3)
    expected3 = 0
    if result3 == expected3:
        print("PASS: Longest substring of empty string is 0")
    else:
        print(f"FAIL: Expected 0, got {result3}")
    
    # Test case 4: String with repeating characters
    s4 = "pwwkew"
    result4 = sw.longest_substring_without_repeating_chars(s4)
    expected4 = 3  # "wke"
    if result4 == expected4:
        print("PASS: Longest substring without repeating characters is 3")
    else:
        print(f"FAIL: Expected 3, got {result4}")

def test_find_all_anagrams():
    """
    Test the find all anagrams algorithm.
    """
    print("\n=== Testing Find All Anagrams ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular strings
    s1 = "cbaebabacd"
    p1 = "abc"
    result1 = sw.find_all_anagrams(s1, p1)
    expected1 = [0, 6]  # "cba" at index 0, "bac" at index 6
    if result1 == expected1:
        print("PASS: Found anagrams at indices [0, 6]")
    else:
        print(f"FAIL: Expected [0, 6], got {result1}")
    
    # Test case 2: Pattern longer than string
    s2 = "abc"
    p2 = "abcd"
    result2 = sw.find_all_anagrams(s2, p2)
    expected2 = []
    if result2 == expected2:
        print("PASS: No anagrams found when pattern is longer than string")
    else:
        print(f"FAIL: Expected [], got {result2}")
    
    # Test case 3: Empty string
    s3 = ""
    p3 = "a"
    result3 = sw.find_all_anagrams(s3, p3)
    expected3 = []
    if result3 == expected3:
        print("PASS: No anagrams found in empty string")
    else:
        print(f"FAIL: Expected [], got {result3}")
    
    # Test case 4: Multiple anagrams
    s4 = "abab"
    p4 = "ab"
    result4 = sw.find_all_anagrams(s4, p4)
    expected4 = [0, 1, 2]  # "ab" at index 0, "ba" at index 1, "ab" at index 2
    if result4 == expected4:
        print("PASS: Found anagrams at indices [0, 1, 2]")
    else:
        print(f"FAIL: Expected [0, 1, 2], got {result4}")

def test_max_sliding_window():
    """
    Test the maximum sliding window algorithm.
    """
    print("\n=== Testing Maximum Sliding Window ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular array
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = sw.max_sliding_window(nums1, k1)
    expected1 = [3, 3, 5, 5, 6, 7]
    if result1 == expected1:
        print("PASS: Maximum sliding window is [3, 3, 5, 5, 6, 7]")
    else:
        print(f"FAIL: Expected [3, 3, 5, 5, 6, 7], got {result1}")
    
    # Test case 2: k = 1
    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    result2 = sw.max_sliding_window(nums2, k2)
    expected2 = [1, 2, 3, 4, 5]
    if result2 == expected2:
        print("PASS: Maximum sliding window with k=1 is [1, 2, 3, 4, 5]")
    else:
        print(f"FAIL: Expected [1, 2, 3, 4, 5], got {result2}")
    
    # Test case 3: Empty array
    nums3 = []
    k3 = 3
    result3 = sw.max_sliding_window(nums3, k3)
    expected3 = []
    if result3 == expected3:
        print("PASS: Maximum sliding window of empty array is []")
    else:
        print(f"FAIL: Expected [], got {result3}")
    
    # Test case 4: k > array length
    nums4 = [1, 2, 3]
    k4 = 4
    result4 = sw.max_sliding_window(nums4, k4)
    expected4 = []
    if result4 == expected4:
        print("PASS: Maximum sliding window with k > array length is []")
    else:
        print(f"FAIL: Expected [], got {result4}")

def test_longest_repeating_character_replacement():
    """
    Test the longest repeating character replacement algorithm.
    """
    print("\n=== Testing Longest Repeating Character Replacement ===")
    sw = SlidingWindow()
    
    # Test case 1: Regular string
    s1 = "AABABBA"
    k1 = 1
    result1 = sw.longest_repeating_character_replacement(s1, k1)
    expected1 = 4  # "AABA" or "ABBA"
    if result1 == expected1:
        print("PASS: Longest repeating character replacement is 4")
    else:
        print(f"FAIL: Expected 4, got {result1}")
    
    # Test case 2: k = 0
    s2 = "ABCDE"
    k2 = 0
    result2 = sw.longest_repeating_character_replacement(s2, k2)
    expected2 = 1  # No replacements allowed
    if result2 == expected2:
        print("PASS: Longest repeating character replacement with k=0 is 1")
    else:
        print(f"FAIL: Expected 1, got {result2}")
    
    # Test case 3: Empty string
    s3 = ""
    k3 = 3
    result3 = sw.longest_repeating_character_replacement(s3, k3)
    expected3 = 0
    if result3 == expected3:
        print("PASS: Longest repeating character replacement of empty string is 0")
    else:
        print(f"FAIL: Expected 0, got {result3}")
    
    # Test case 4: k >= string length
    s4 = "ABC"
    k4 = 3
    result4 = sw.longest_repeating_character_replacement(s4, k4)
    expected4 = 3  # Can replace all characters
    if result4 == expected4:
        print("PASS: Longest repeating character replacement with k >= string length is 3")
    else:
        print(f"FAIL: Expected 3, got {result4}")

def main():
    """
    Main method to run the tests.
    """
    print("Running Sliding Window Tests...")
    print("Using implementation:", "SlidingWindowSolution" if SlidingWindow == SlidingWindowSolution else "SlidingWindowTemplate")
    
    test_max_sum_subarray()
    test_min_size_subarray_sum()
    test_longest_substring_without_repeating_chars()
    test_find_all_anagrams()
    test_max_sliding_window()
    test_longest_repeating_character_replacement()
    
    print("All tests completed.")

if __name__ == "__main__":
    main()
