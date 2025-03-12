"""
SlidingWindow implementation.
This class provides a blueprint for implementing sliding window algorithms with
various operations for solving different types of problems.
"""
from SlidingWindow.Python.node import Node
from collections import deque, defaultdict

class SlidingWindow:
    def find_max_sum_subarray(self, arr, k):
        """
        Find the maximum sum subarray of size k.
        
        Args:
            arr: The input array
            k: The size of the window
            
        Returns:
            The maximum sum of any subarray of size k
        """
        if not arr or k <= 0 or k > len(arr):
            return 0
        
        window_sum = 0
        max_sum = float('-inf')
        
        # First window
        for i in range(k):
            window_sum += arr[i]
        
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(arr)):
            window_sum = window_sum + arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum
    
    def find_min_subarray_length(self, arr, target):
        """
        Find the smallest subarray with a sum greater than or equal to the target.
        
        Args:
            arr: The input array
            target: The target sum
            
        Returns:
            The length of the smallest subarray with sum >= target, or 0 if no such subarray exists
        """
        if not arr or target <= 0:
            return 0
        
        window_sum = 0
        min_length = float('inf')
        window_start = 0
        
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            
            # Shrink the window as small as possible while maintaining the sum >= target
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        
        return min_length if min_length != float('inf') else 0
    
    def find_longest_substring_k_distinct(self, s, k):
        """
        Find the longest substring with at most k distinct characters.
        
        Args:
            s: The input string
            k: The maximum number of distinct characters
            
        Returns:
            The length of the longest substring with at most k distinct characters
        """
        if not s or k <= 0:
            return 0
        
        char_frequency = {}
        window_start = 0
        max_length = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1
            
            # Shrink the window if we have more than k distinct characters
            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
    
    def find_longest_substring_no_repeat(self, s):
        """
        Find the longest substring without repeating characters.
        
        Args:
            s: The input string
            
        Returns:
            The length of the longest substring without repeating characters
        """
        if not s:
            return 0
        
        char_index_map = {}
        window_start = 0
        max_length = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # If the character is already in the window, shrink the window
            if right_char in char_index_map:
                # Move the window start to the right of the last occurrence of the character
                window_start = max(window_start, char_index_map[right_char] + 1)
            
            # Update the index of the character
            char_index_map[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
    
    def find_anagrams(self, s, pattern):
        """
        Find all anagrams of a pattern in a string.
        
        Args:
            s: The input string
            pattern: The pattern to find anagrams of
            
        Returns:
            A list of starting indices of all anagrams of the pattern in the string
        """
        if not s or not pattern or len(s) < len(pattern):
            return []
        
        pattern_freq = {}
        for char in pattern:
            pattern_freq[char] = pattern_freq.get(char, 0) + 1
        
        window_start = 0
        matched = 0
        result = []
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # If the character is in the pattern, decrement its frequency
            if right_char in pattern_freq:
                pattern_freq[right_char] -= 1
                if pattern_freq[right_char] == 0:
                    matched += 1
            
            # If all characters in the pattern are matched, we found an anagram
            if matched == len(pattern_freq):
                result.append(window_start)
            
            # If the window size is equal to the pattern length, shrink the window
            if window_end >= len(pattern) - 1:
                left_char = s[window_start]
                window_start += 1
                
                # If the character is in the pattern, update the frequency and matched count
                if left_char in pattern_freq:
                    if pattern_freq[left_char] == 0:
                        matched -= 1
                    pattern_freq[left_char] += 1
        
        return result
    
    def find_max_in_sliding_window(self, arr, k):
        """
        Find the maximum of each subarray of size k.
        
        Args:
            arr: The input array
            k: The size of the window
            
        Returns:
            A list containing the maximum of each subarray of size k
        """
        if not arr or k <= 0 or k > len(arr):
            return []
        
        result = []
        window = deque()
        
        for i in range(len(arr)):
            # Remove elements that are out of the current window
            while window and window[0] <= i - k:
                window.popleft()
            
            # Remove elements smaller than the current element from the back
            while window and arr[window[-1]] < arr[i]:
                window.pop()
            
            # Add the current element to the window
            window.append(i)
            
            # If the window has reached its size, add the maximum to the result
            if i >= k - 1:
                result.append(arr[window[0]])
        
        return result
    
    def find_min_window_substring(self, s, pattern):
        """
        Find the minimum window substring that contains all characters of the pattern.
        
        Args:
            s: The input string
            pattern: The pattern string
            
        Returns:
            The minimum window substring, or an empty string if no such substring exists
        """
        if not s or not pattern or len(s) < len(pattern):
            return ""
        
        pattern_freq = {}
        for char in pattern:
            pattern_freq[char] = pattern_freq.get(char, 0) + 1
        
        window_start = 0
        matched = 0
        min_length = float('inf')
        substr_start = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # If the character is in the pattern, decrement its frequency
            if right_char in pattern_freq:
                pattern_freq[right_char] -= 1
                if pattern_freq[right_char] >= 0:
                    matched += 1
            
            # If all characters in the pattern are matched, try to shrink the window
            while matched == len(pattern):
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                
                left_char = s[window_start]
                window_start += 1
                
                # If the character is in the pattern, update the frequency and matched count
                if left_char in pattern_freq:
                    if pattern_freq[left_char] == 0:
                        matched -= 1
                    pattern_freq[left_char] += 1
        
        return s[substr_start:substr_start + min_length] if min_length != float('inf') else ""
    
    def find_max_profit(self, prices):
        """
        Find the maximum profit by buying and selling a stock once.
        
        Args:
            prices: The array of stock prices
            
        Returns:
            The maximum profit
        """
        if not prices or len(prices) < 2:
            return 0
        
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
    
    def find_longest_ones_subarray(self, arr, k):
        """
        Find the longest subarray with ones after replacing at most k zeros.
        
        Args:
            arr: The input array (containing only 0s and 1s)
            k: The maximum number of zeros that can be replaced
            
        Returns:
            The length of the longest subarray with ones after replacing at most k zeros
        """
        if not arr:
            return 0
        
        window_start = 0
        max_length = 0
        max_ones_count = 0
        
        for window_end in range(len(arr)):
            if arr[window_end] == 1:
                max_ones_count += 1
            
            # If the number of zeros in the window is more than k, shrink the window
            if (window_end - window_start + 1 - max_ones_count) > k:
                if arr[window_start] == 1:
                    max_ones_count -= 1
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
