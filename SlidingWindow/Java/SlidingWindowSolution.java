package SlidingWindow.Java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

/**
 * Complete implementation of Sliding Window algorithms.
 * This class provides a reference solution for the SlidingWindow blueprint.
 * You can use this as a guide if you get stuck with your implementation.
 */
public class SlidingWindowSolution {
    
    /**
     * Find the maximum sum subarray of size k.
     * 
     * @param arr The input array
     * @param k The size of the window
     * @return The maximum sum of any subarray of size k
     */
    public int findMaxSumSubarray(int[] arr, int k) {
        if (arr == null || arr.length == 0 || k <= 0 || k > arr.length) {
            return 0;
        }
        
        int maxSum = 0;
        int windowSum = 0;
        
        // Calculate sum of first k elements
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        
        maxSum = windowSum;
        
        // Slide the window and update maxSum
        for (int i = k; i < arr.length; i++) {
            windowSum = windowSum - arr[i - k] + arr[i];
            maxSum = Math.max(maxSum, windowSum);
        }
        
        return maxSum;
    }
    
    /**
     * Find the smallest subarray with a sum greater than or equal to the target.
     * 
     * @param arr The input array
     * @param target The target sum
     * @return The length of the smallest subarray with sum >= target, or 0 if no such subarray exists
     */
    public int findMinSubarrayLength(int[] arr, int target) {
        if (arr == null || arr.length == 0 || target <= 0) {
            return 0;
        }
        
        int minLength = Integer.MAX_VALUE;
        int windowSum = 0;
        int windowStart = 0;
        
        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            windowSum += arr[windowEnd];
            
            // Shrink the window as small as possible while maintaining the sum >= target
            while (windowSum >= target) {
                minLength = Math.min(minLength, windowEnd - windowStart + 1);
                windowSum -= arr[windowStart];
                windowStart++;
            }
        }
        
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }
    
    /**
     * Find the longest substring with at most k distinct characters.
     * 
     * @param str The input string
     * @param k The maximum number of distinct characters
     * @return The length of the longest substring with at most k distinct characters
     */
    public int findLongestSubstringKDistinct(String str, int k) {
        if (str == null || str.length() == 0 || k <= 0) {
            return 0;
        }
        
        int maxLength = 0;
        int windowStart = 0;
        Map<Character, Integer> charFrequency = new HashMap<>();
        
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            charFrequency.put(rightChar, charFrequency.getOrDefault(rightChar, 0) + 1);
            
            // Shrink the window if we have more than k distinct characters
            while (charFrequency.size() > k) {
                char leftChar = str.charAt(windowStart);
                charFrequency.put(leftChar, charFrequency.get(leftChar) - 1);
                if (charFrequency.get(leftChar) == 0) {
                    charFrequency.remove(leftChar);
                }
                windowStart++;
            }
            
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        
        return maxLength;
    }
    
    /**
     * Find the longest substring without repeating characters.
     * 
     * @param str The input string
     * @return The length of the longest substring without repeating characters
     */
    public int findLongestSubstringNoRepeat(String str) {
        if (str == null || str.length() == 0) {
            return 0;
        }
        
        int maxLength = 0;
        int windowStart = 0;
        Map<Character, Integer> charIndexMap = new HashMap<>();
        
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            
            // If the character is already in the window, shrink the window
            if (charIndexMap.containsKey(rightChar)) {
                // Move the window start to the right of the last occurrence of the character
                windowStart = Math.max(windowStart, charIndexMap.get(rightChar) + 1);
            }
            
            // Update the index of the character
            charIndexMap.put(rightChar, windowEnd);
            
            // Update the maximum length
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        
        return maxLength;
    }
    
    /**
     * Find all anagrams of a pattern in a string.
     * 
     * @param str The input string
     * @param pattern The pattern to find anagrams of
     * @return An array of starting indices of all anagrams of the pattern in the string
     */
    public int[] findAnagrams(String str, String pattern) {
        if (str == null || pattern == null || str.length() < pattern.length()) {
            return new int[0];
        }
        
        List<Integer> resultIndices = new ArrayList<>();
        Map<Character, Integer> patternFrequency = new HashMap<>();
        Map<Character, Integer> windowFrequency = new HashMap<>();
        
        // Build the frequency map for the pattern
        for (char c : pattern.toCharArray()) {
            patternFrequency.put(c, patternFrequency.getOrDefault(c, 0) + 1);
        }
        
        int windowStart = 0;
        int matched = 0;
        
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            
            // Add the right character to the window frequency map
            windowFrequency.put(rightChar, windowFrequency.getOrDefault(rightChar, 0) + 1);
            
            // If the frequency of the current character matches with the pattern, increment the matched count
            if (patternFrequency.containsKey(rightChar) && windowFrequency.get(rightChar).equals(patternFrequency.get(rightChar))) {
                matched++;
            }
            
            // If we have found an anagram
            if (matched == patternFrequency.size()) {
                resultIndices.add(windowStart);
            }
            
            // Shrink the window if its size is equal to the pattern length
            if (windowEnd >= pattern.length() - 1) {
                char leftChar = str.charAt(windowStart);
                
                // If the frequency of the left character matches with the pattern, decrement the matched count
                if (patternFrequency.containsKey(leftChar) && windowFrequency.get(leftChar).equals(patternFrequency.get(leftChar))) {
                    matched--;
                }
                
                // Remove the left character from the window frequency map
                windowFrequency.put(leftChar, windowFrequency.get(leftChar) - 1);
                if (windowFrequency.get(leftChar) == 0) {
                    windowFrequency.remove(leftChar);
                }
                
                windowStart++;
            }
        }
        
        // Convert the list to an array
        int[] result = new int[resultIndices.size()];
        for (int i = 0; i < resultIndices.size(); i++) {
            result[i] = resultIndices.get(i);
        }
        
        return result;
    }
    
    /**
     * Find the maximum of each subarray of size k.
     * 
     * @param arr The input array
     * @param k The size of the window
     * @return An array containing the maximum of each subarray of size k
     */
    public int[] findMaxInSlidingWindow(int[] arr, int k) {
        if (arr == null || arr.length == 0 || k <= 0 || k > arr.length) {
            return new int[0];
        }
        
        int[] result = new int[arr.length - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();
        
        for (int i = 0; i < arr.length; i++) {
            // Remove elements outside the current window
            while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.pollFirst();
            }
            
            // Remove elements smaller than the current element
            while (!deque.isEmpty() && arr[deque.peekLast()] < arr[i]) {
                deque.pollLast();
            }
            
            // Add the current element
            deque.offerLast(i);
            
            // Add the maximum element to the result
            if (i >= k - 1) {
                result[i - k + 1] = arr[deque.peekFirst()];
            }
        }
        
        return result;
    }
    
    /**
     * Find the minimum window substring that contains all characters of the pattern.
     * 
     * @param str The input string
     * @param pattern The pattern string
     * @return The minimum window substring, or an empty string if no such substring exists
     */
    public String findMinWindowSubstring(String str, String pattern) {
        if (str == null || pattern == null || str.length() < pattern.length()) {
            return "";
        }
        
        Map<Character, Integer> patternFrequency = new HashMap<>();
        Map<Character, Integer> windowFrequency = new HashMap<>();
        
        // Build the frequency map for the pattern
        for (char c : pattern.toCharArray()) {
            patternFrequency.put(c, patternFrequency.getOrDefault(c, 0) + 1);
        }
        
        int windowStart = 0;
        int matched = 0;
        int minLength = Integer.MAX_VALUE;
        int substrStart = 0;
        
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            
            // Add the right character to the window frequency map
            windowFrequency.put(rightChar, windowFrequency.getOrDefault(rightChar, 0) + 1);
            
            // If the frequency of the current character matches with the pattern, increment the matched count
            if (patternFrequency.containsKey(rightChar) && windowFrequency.get(rightChar) <= patternFrequency.get(rightChar)) {
                matched++;
            }
            
            // Shrink the window if we have found all characters
            while (matched == pattern.length()) {
                // Update the minimum window
                if (windowEnd - windowStart + 1 < minLength) {
                    minLength = windowEnd - windowStart + 1;
                    substrStart = windowStart;
                }
                
                char leftChar = str.charAt(windowStart);
                
                // Remove the left character from the window frequency map
                windowFrequency.put(leftChar, windowFrequency.get(leftChar) - 1);
                
                // If the frequency of the left character is less than the pattern, decrement the matched count
                if (patternFrequency.containsKey(leftChar) && windowFrequency.get(leftChar) < patternFrequency.get(leftChar)) {
                    matched--;
                }
                
                windowStart++;
            }
        }
        
        return minLength == Integer.MAX_VALUE ? "" : str.substring(substrStart, substrStart + minLength);
    }
    
    /**
     * Find the maximum profit by buying and selling a stock once.
     * 
     * @param prices The array of stock prices
     * @return The maximum profit
     */
    public int findMaxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        
        int maxProfit = 0;
        int minPrice = prices[0];
        
        for (int i = 1; i < prices.length; i++) {
            // Update the minimum price
            minPrice = Math.min(minPrice, prices[i]);
            
            // Update the maximum profit
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        
        return maxProfit;
    }
    
    /**
     * Find the longest subarray with ones after replacing at most k zeros.
     * 
     * @param arr The input array (containing only 0s and 1s)
     * @param k The maximum number of zeros that can be replaced
     * @return The length of the longest subarray with ones after replacing at most k zeros
     */
    public int findLongestOnesSubarray(int[] arr, int k) {
        if (arr == null || arr.length == 0 || k < 0) {
            return 0;
        }
        
        int maxLength = 0;
        int windowStart = 0;
        int zeroCount = 0;
        
        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            // If the current element is 0, increment the zero count
            if (arr[windowEnd] == 0) {
                zeroCount++;
            }
            
            // Shrink the window if we have more than k zeros
            while (zeroCount > k) {
                if (arr[windowStart] == 0) {
                    zeroCount--;
                }
                windowStart++;
            }
            
            // Update the maximum length
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        
        return maxLength;
    }
}
