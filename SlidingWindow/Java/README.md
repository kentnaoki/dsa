# Sliding Window Implementation

This directory contains a blueprint for implementing Sliding Window algorithms in Java. The implementation includes:

- `Node.java`: A complete implementation of the Node class for linked list operations
- `SlidingWindow.java`: A blueprint with method stubs for the Sliding Window operations
- `SlidingWindowTest.java`: A test class to verify the implementation
- `SlidingWindowSolution.java`: A complete reference implementation that you can use if you get stuck

## Task

Your task is to implement the methods in the `SlidingWindow.java` file. The methods are already defined with appropriate comments explaining what each method should do. Look for the `TODO` comments in the file to see what needs to be implemented.

## Key Operations to Implement

1. **findMaxSumSubarray(int[] arr, int k)**: Find the maximum sum subarray of size k
2. **findMinSubarrayLength(int[] arr, int target)**: Find the smallest subarray with a sum greater than or equal to the target
3. **findLongestSubstringKDistinct(String str, int k)**: Find the longest substring with at most k distinct characters
4. **findLongestSubstringNoRepeat(String str)**: Find the longest substring without repeating characters
5. **findAnagrams(String str, String pattern)**: Find all anagrams of a pattern in a string
6. **findMaxInSlidingWindow(int[] arr, int k)**: Find the maximum of each subarray of size k
7. **findMinWindowSubstring(String str, String pattern)**: Find the minimum window substring that contains all characters of the pattern
8. **findMaxProfit(int[] prices)**: Find the maximum profit by buying and selling a stock once
9. **findLongestOnesSubarray(int[] arr, int k)**: Find the longest subarray with ones after replacing at most k zeros

## Running the Tests

You can run the tests in two ways:

### Option 1: Using the provided script

From the root directory, run:

```bash
./SlidingWindow/Java/run_tests.sh
```

This script will compile all the Java files and run the tests for you.

### Option 2: Manual compilation and execution

Alternatively, you can compile and run the tests manually with the following commands from the root directory:

```bash
# Compile the Java files
javac SlidingWindow/Java/*.java

# Run the tests
java SlidingWindow.Java.SlidingWindowTest
```

The test class will run various tests on your implementation and print the results to the console. Each test will indicate whether it passed or failed, helping you identify any issues with your implementation.

## Sliding Window Technique

The Sliding Window technique is a method that involves creating a window of elements and sliding it through an array or string to solve problems efficiently. It's particularly useful for problems involving subarrays or substrings.

Key properties of the Sliding Window technique:

1. It reduces the time complexity from O(n²) to O(n) for many problems
2. It's used to process arrays or strings in a sequential manner
3. The window size can be fixed or variable, depending on the problem
4. It's particularly useful for problems involving subarrays or substrings with certain properties

## Implementation Tips

- For fixed-size window problems (like finding the maximum sum subarray of size k), initialize the window with the first k elements, then slide the window one element at a time
- For variable-size window problems (like finding the smallest subarray with sum >= target), use two pointers to represent the window boundaries and adjust them based on the problem constraints
- For string problems, use a hash map or array to keep track of character frequencies
- For finding the maximum in a sliding window, consider using a deque (double-ended queue) to efficiently track the maximum element
- For problems involving anagrams or pattern matching, compare character frequencies rather than the actual strings
- For problems involving stock prices, keep track of the minimum price seen so far and update the maximum profit

Good luck with your implementation!
