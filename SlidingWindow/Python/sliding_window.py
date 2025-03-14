"""
Sliding Window algorithm implementation.
This class provides a blueprint for implementing various sliding window problems.
"""
from collections import defaultdict, deque
import sys

class SlidingWindow:
    def __init__(self):
        """
        Constructor to create a new SlidingWindow instance.
        """
        pass
    
    def max_sum_subarray(self, arr, k):
        """
        Find the maximum sum of a subarray of size k.
        
        Args:
            arr: Input array of integers
            k: Size of the sliding window
            
        Returns:
            Maximum sum of a subarray of size k
        """
        # TODO: Implement this method
        # 1. Check if the input array is valid and k is within bounds
        # 2. Initialize variables for max_sum and window_sum
        # 3. Calculate the sum of the first window
        # 4. Slide the window and update max_sum
        # 5. Return the maximum sum
        if arr == None or len(arr) < k:
            return 0
        left = 0
        right = k - 1

        max_sum = -sys.maxsize - 1
        while right < len(arr):
            max_sum = max(max_sum, sum(arr[left:right+1]))
            left += 1
            right += 1
        return max_sum

    
    def min_size_subarray_sum(self, arr, target_sum):
        """
        Find the minimum size subarray with a sum at least target_sum.
        
        Args:
            arr: Input array of positive integers
            target_sum: Target sum
            
        Returns:
            Minimum size of a subarray with sum at least target_sum, or 0 if no such subarray exists
        """
        # TODO: Implement this method
        # 1. Check if the input array is valid and target_sum is positive
        # 2. Initialize variables for min_length, window_sum, and start pointer
        # 3. Slide the window and update min_length
        # 4. Return the minimum length, or 0 if no valid subarray is found
        if arr == None:
            return 0

        left = 0
        window_sum = 0
        min_size = sys.maxsize

        for right in range(len(arr)):
            window_sum += arr[right]
            while window_sum >= target_sum:
                min_size = min(min_size, right - left + 1)
                window_sum -= arr[left]
                left += 1

        return min_size if min_size != sys.maxsize else 0
    
    def longest_substring_without_repeating_chars(self, s):
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        # TODO: Implement this method
        # 1. Check if the input string is valid
        # 2. Initialize variables for max_length, start pointer, and character index map
        # 3. Slide the window and update max_length
        # 4. Return the maximum length
        if s == None:
            return 0

        left = 0
        max_length = 0
        char_index_map = {}

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
    
    def find_all_anagrams(self, s, p):
        """
        Find all start indices of anagrams of p in s.
        
        Args:
            s: Input string
            p: Pattern string
            
        Returns:
            List of start indices of anagrams of p in s
        """
        # TODO: Implement this method
        # 1. Check if the input strings are valid
        # 2. Initialize variables for result, pattern count, and window count
        # 3. Count characters in the pattern
        # 4. Initialize the first window
        # 5. Slide the window and check for anagrams
        # 6. Return the list of start indices
        if s == None or len(s) < len(p):
            return []
        pattern_map = self.create_map(p)
        left = 0
        right = len(p) - 1

        result = []
        current_map = self.create_map(s[left:right+1])
        while right < len(s):
            if left > 0:
                left_char = s[left - 1]
                new_char = s[right]
                current_map[left_char] = current_map.get(left_char, 0) - 1
                if current_map[left_char] == 0:
                    del current_map[left_char]
                current_map[new_char] = current_map.get(new_char, 0) + 1
            if current_map == pattern_map:
                result.append(left)
            right += 1
            left += 1
            
        print(s, p)

        return result
    
    def create_map(self, word):
        map = {}
        for c in word:
            map[c] = map.get(c, 0) + 1
        return map


    def max_sliding_window(self, nums, k):
        """
        Find the maximum element in each sliding window of size k.
        
        Args:
            nums: Input array of integers
            k: Size of the sliding window
            
        Returns:
            Array of maximum elements in each sliding window
        """
        # TODO: Implement this method
        # 1. Check if the input array is valid and k is within bounds
        # 2. Initialize variables for result and deque (to store indices)
        # 3. Process each element in the array:
        #    a. Remove elements outside the window
        #    b. Remove smaller elements as they are not useful
        #    c. Add current element
        #    d. Add maximum element to result if we have a complete window
        # 4. Return the result array
        return []
    
    def longest_repeating_character_replacement(self, s, k):
        """
        Find the length of the longest substring containing the same letter after replacing at most k characters.
        
        Args:
            s: Input string
            k: Maximum number of characters to replace
            
        Returns:
            Length of the longest substring containing the same letter after replacing at most k characters
        """
        # TODO: Implement this method
        # 1. Check if the input string is valid
        # 2. Initialize variables for max_length, max_count, character count, and start pointer
        # 3. Slide the window:
        #    a. Update character count
        #    b. Update max_count (most frequent character in the window)
        #    c. If the number of characters to replace exceeds k, shrink the window
        #    d. Update max_length
        # 4. Return the maximum length
        return 0
