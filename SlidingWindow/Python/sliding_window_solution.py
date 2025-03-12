"""
Complete implementation of Sliding Window algorithms.
This class provides a reference solution for the Sliding Window blueprint.
You can use this as a guide if you get stuck with your implementation.
"""
from collections import defaultdict, deque

class SlidingWindowSolution:
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
        if not arr or k <= 0 or k > len(arr):
            return 0
        
        # Initialize variables
        max_sum = 0
        window_sum = 0
        
        # Calculate sum of first window
        for i in range(k):
            window_sum += arr[i]
        
        max_sum = window_sum
        
        # Slide the window and update max_sum
        for i in range(k, len(arr)):
            window_sum = window_sum + arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)
        
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
        if not arr or target_sum <= 0:
            return 0
        
        # Initialize variables
        min_length = float('inf')
        window_sum = 0
        start = 0
        
        # Slide the window
        for end in range(len(arr)):
            window_sum += arr[end]
            
            # Shrink the window as small as possible while maintaining the sum >= target_sum
            while window_sum >= target_sum:
                min_length = min(min_length, end - start + 1)
                window_sum -= arr[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0
    
    def longest_substring_without_repeating_chars(self, s):
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        if not s:
            return 0
        
        # Initialize variables
        max_length = 0
        start = 0
        char_index_map = {}
        
        # Slide the window
        for end in range(len(s)):
            # If the character is already in the window, update the start pointer
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            
            # Update the character's index
            char_index_map[s[end]] = end
            
            # Update max_length
            max_length = max(max_length, end - start + 1)
        
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
        if not s or not p or len(s) < len(p):
            return []
        
        # Initialize variables
        result = []
        p_count = defaultdict(int)
        window_count = defaultdict(int)
        
        # Count characters in pattern
        for char in p:
            p_count[char] += 1
        
        # Initialize window
        for i in range(len(p)):
            window_count[s[i]] += 1
        
        # Check if the initial window is an anagram
        if window_count == p_count:
            result.append(0)
        
        # Slide the window
        for i in range(len(p), len(s)):
            # Add the new character to the window
            window_count[s[i]] += 1
            
            # Remove the leftmost character from the window
            window_count[s[i - len(p)]] -= 1
            
            # If the count becomes 0, remove the character from the dictionary
            if window_count[s[i - len(p)]] == 0:
                del window_count[s[i - len(p)]]
            
            # Check if the current window is an anagram
            if window_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
    
    def max_sliding_window(self, nums, k):
        """
        Find the maximum element in each sliding window of size k.
        
        Args:
            nums: Input array of integers
            k: Size of the sliding window
            
        Returns:
            Array of maximum elements in each sliding window
        """
        if not nums or k <= 0 or k > len(nums):
            return []
        
        # Initialize variables
        result = []
        deq = deque()  # Store indices of elements in decreasing order
        
        for i in range(len(nums)):
            # Remove elements outside the window
            while deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove smaller elements as they are not useful
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add current element
            deq.append(i)
            
            # Add maximum element to result if we have a complete window
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
    
    def longest_repeating_character_replacement(self, s, k):
        """
        Find the length of the longest substring containing the same letter after replacing at most k characters.
        
        Args:
            s: Input string
            k: Maximum number of characters to replace
            
        Returns:
            Length of the longest substring containing the same letter after replacing at most k characters
        """
        if not s:
            return 0
        
        # Initialize variables
        max_length = 0
        max_count = 0
        char_count = defaultdict(int)
        start = 0
        
        # Slide the window
        for end in range(len(s)):
            # Update character count
            char_count[s[end]] += 1
            
            # Update max_count (most frequent character in the window)
            max_count = max(max_count, char_count[s[end]])
            
            # If the number of characters to replace exceeds k, shrink the window
            if end - start + 1 - max_count > k:
                char_count[s[start]] -= 1
                start += 1
            
            # Update max_length
            max_length = max(max_length, end - start + 1)
        
        return max_length
