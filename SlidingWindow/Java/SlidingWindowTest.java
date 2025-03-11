package SlidingWindow.Java;

import java.util.Arrays;

/**
 * Test class for the SlidingWindow implementation.
 * This class provides methods to test various operations of the SlidingWindow algorithms.
 */
public class SlidingWindowTest {
    
    /**
     * Main method to run the tests.
     * 
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        System.out.println("Running Sliding Window Tests...");
        
        testMaxSumSubarray();
        testMinSubarrayLength();
        testLongestSubstringKDistinct();
        testLongestSubstringNoRepeat();
        testFindAnagrams();
        testMaxInSlidingWindow();
        testMinWindowSubstring();
        testMaxProfit();
        testLongestOnesSubarray();
        
        System.out.println("All tests completed.");
    }
    
    /**
     * Test the findMaxSumSubarray operation.
     */
    private static void testMaxSumSubarray() {
        System.out.println("\n=== Testing Maximum Sum Subarray ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular array
        int[] arr1 = {2, 1, 5, 1, 3, 2};
        int k1 = 3;
        int result1 = sw.findMaxSumSubarray(arr1, k1);
        System.out.println("Maximum sum subarray of size " + k1 + " in [2, 1, 5, 1, 3, 2]: " + result1);
        if (result1 == 9) {
            System.out.println("PASS: Maximum sum is 9");
        } else {
            System.out.println("FAIL: Maximum sum should be 9, but got " + result1);
        }
        
        // Test case 2: Array with negative numbers
        int[] arr2 = {-2, -3, 4, -1, -2, 1, 5, -3};
        int k2 = 3;
        int result2 = sw.findMaxSumSubarray(arr2, k2);
        System.out.println("Maximum sum subarray of size " + k2 + " in [-2, -3, 4, -1, -2, 1, 5, -3]: " + result2);
        if (result2 == 4) {
            System.out.println("PASS: Maximum sum is 4");
        } else {
            System.out.println("FAIL: Maximum sum should be 4, but got " + result2);
        }
    }
    
    /**
     * Test the findMinSubarrayLength operation.
     */
    private static void testMinSubarrayLength() {
        System.out.println("\n=== Testing Minimum Subarray Length ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular array
        int[] arr1 = {2, 1, 5, 2, 3, 2};
        int target1 = 7;
        int result1 = sw.findMinSubarrayLength(arr1, target1);
        System.out.println("Minimum subarray length with sum >= " + target1 + " in [2, 1, 5, 2, 3, 2]: " + result1);
        if (result1 == 2) {
            System.out.println("PASS: Minimum length is 2");
        } else {
            System.out.println("FAIL: Minimum length should be 2, but got " + result1);
        }
        
        // Test case 2: No subarray with sum >= target
        int[] arr2 = {1, 2, 3, 4, 5};
        int target2 = 20;
        int result2 = sw.findMinSubarrayLength(arr2, target2);
        System.out.println("Minimum subarray length with sum >= " + target2 + " in [1, 2, 3, 4, 5]: " + result2);
        if (result2 == 0) {
            System.out.println("PASS: No subarray with sum >= " + target2);
        } else {
            System.out.println("FAIL: Should return 0, but got " + result2);
        }
    }
    
    /**
     * Test the findLongestSubstringKDistinct operation.
     */
    private static void testLongestSubstringKDistinct() {
        System.out.println("\n=== Testing Longest Substring with K Distinct Characters ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular string
        String str1 = "araaci";
        int k1 = 2;
        int result1 = sw.findLongestSubstringKDistinct(str1, k1);
        System.out.println("Longest substring with at most " + k1 + " distinct characters in \"" + str1 + "\": " + result1);
        if (result1 == 4) {
            System.out.println("PASS: Longest substring length is 4");
        } else {
            System.out.println("FAIL: Longest substring length should be 4, but got " + result1);
        }
        
        // Test case 2: String with all distinct characters
        String str2 = "abcdef";
        int k2 = 3;
        int result2 = sw.findLongestSubstringKDistinct(str2, k2);
        System.out.println("Longest substring with at most " + k2 + " distinct characters in \"" + str2 + "\": " + result2);
        if (result2 == 3) {
            System.out.println("PASS: Longest substring length is 3");
        } else {
            System.out.println("FAIL: Longest substring length should be 3, but got " + result2);
        }
    }
    
    /**
     * Test the findLongestSubstringNoRepeat operation.
     */
    private static void testLongestSubstringNoRepeat() {
        System.out.println("\n=== Testing Longest Substring without Repeating Characters ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular string
        String str1 = "abcabcbb";
        int result1 = sw.findLongestSubstringNoRepeat(str1);
        System.out.println("Longest substring without repeating characters in \"" + str1 + "\": " + result1);
        if (result1 == 3) {
            System.out.println("PASS: Longest substring length is 3");
        } else {
            System.out.println("FAIL: Longest substring length should be 3, but got " + result1);
        }
        
        // Test case 2: String with all repeating characters
        String str2 = "bbbbb";
        int result2 = sw.findLongestSubstringNoRepeat(str2);
        System.out.println("Longest substring without repeating characters in \"" + str2 + "\": " + result2);
        if (result2 == 1) {
            System.out.println("PASS: Longest substring length is 1");
        } else {
            System.out.println("FAIL: Longest substring length should be 1, but got " + result2);
        }
    }
    
    /**
     * Test the findAnagrams operation.
     */
    private static void testFindAnagrams() {
        System.out.println("\n=== Testing Find Anagrams ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular string and pattern
        String str1 = "cbaebabacd";
        String pattern1 = "abc";
        int[] result1 = sw.findAnagrams(str1, pattern1);
        System.out.println("Anagrams of \"" + pattern1 + "\" in \"" + str1 + "\": " + Arrays.toString(result1));
        if (result1.length == 2 && result1[0] == 0 && result1[1] == 6) {
            System.out.println("PASS: Found anagrams at indices [0, 6]");
        } else {
            System.out.println("FAIL: Should find anagrams at indices [0, 6], but got " + Arrays.toString(result1));
        }
        
        // Test case 2: No anagrams
        String str2 = "hello";
        String pattern2 = "world";
        int[] result2 = sw.findAnagrams(str2, pattern2);
        System.out.println("Anagrams of \"" + pattern2 + "\" in \"" + str2 + "\": " + Arrays.toString(result2));
        if (result2.length == 0) {
            System.out.println("PASS: No anagrams found");
        } else {
            System.out.println("FAIL: Should find no anagrams, but got " + Arrays.toString(result2));
        }
    }
    
    /**
     * Test the findMaxInSlidingWindow operation.
     */
    private static void testMaxInSlidingWindow() {
        System.out.println("\n=== Testing Maximum in Sliding Window ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular array
        int[] arr1 = {1, 3, -1, -3, 5, 3, 6, 7};
        int k1 = 3;
        int[] result1 = sw.findMaxInSlidingWindow(arr1, k1);
        System.out.println("Maximum in sliding window of size " + k1 + " in [1, 3, -1, -3, 5, 3, 6, 7]: " + Arrays.toString(result1));
        int[] expected1 = {3, 3, 5, 5, 6, 7};
        if (Arrays.equals(result1, expected1)) {
            System.out.println("PASS: Maximum in sliding window is " + Arrays.toString(expected1));
        } else {
            System.out.println("FAIL: Maximum in sliding window should be " + Arrays.toString(expected1) + ", but got " + Arrays.toString(result1));
        }
        
        // Test case 2: Small array
        int[] arr2 = {1, 2, 3, 4, 5};
        int k2 = 2;
        int[] result2 = sw.findMaxInSlidingWindow(arr2, k2);
        System.out.println("Maximum in sliding window of size " + k2 + " in [1, 2, 3, 4, 5]: " + Arrays.toString(result2));
        int[] expected2 = {2, 3, 4, 5};
        if (Arrays.equals(result2, expected2)) {
            System.out.println("PASS: Maximum in sliding window is " + Arrays.toString(expected2));
        } else {
            System.out.println("FAIL: Maximum in sliding window should be " + Arrays.toString(expected2) + ", but got " + Arrays.toString(result2));
        }
    }
    
    /**
     * Test the findMinWindowSubstring operation.
     */
    private static void testMinWindowSubstring() {
        System.out.println("\n=== Testing Minimum Window Substring ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular string and pattern
        String str1 = "ADOBECODEBANC";
        String pattern1 = "ABC";
        String result1 = sw.findMinWindowSubstring(str1, pattern1);
        System.out.println("Minimum window substring of \"" + pattern1 + "\" in \"" + str1 + "\": \"" + result1 + "\"");
        if (result1.equals("BANC")) {
            System.out.println("PASS: Minimum window substring is \"BANC\"");
        } else {
            System.out.println("FAIL: Minimum window substring should be \"BANC\", but got \"" + result1 + "\"");
        }
        
        // Test case 2: No window substring
        String str2 = "hello";
        String pattern2 = "world";
        String result2 = sw.findMinWindowSubstring(str2, pattern2);
        System.out.println("Minimum window substring of \"" + pattern2 + "\" in \"" + str2 + "\": \"" + result2 + "\"");
        if (result2.equals("")) {
            System.out.println("PASS: No window substring found");
        } else {
            System.out.println("FAIL: Should find no window substring, but got \"" + result2 + "\"");
        }
    }
    
    /**
     * Test the findMaxProfit operation.
     */
    private static void testMaxProfit() {
        System.out.println("\n=== Testing Maximum Profit ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular prices
        int[] prices1 = {7, 1, 5, 3, 6, 4};
        int result1 = sw.findMaxProfit(prices1);
        System.out.println("Maximum profit in [7, 1, 5, 3, 6, 4]: " + result1);
        if (result1 == 5) {
            System.out.println("PASS: Maximum profit is 5");
        } else {
            System.out.println("FAIL: Maximum profit should be 5, but got " + result1);
        }
        
        // Test case 2: Decreasing prices
        int[] prices2 = {7, 6, 4, 3, 1};
        int result2 = sw.findMaxProfit(prices2);
        System.out.println("Maximum profit in [7, 6, 4, 3, 1]: " + result2);
        if (result2 == 0) {
            System.out.println("PASS: Maximum profit is 0");
        } else {
            System.out.println("FAIL: Maximum profit should be 0, but got " + result2);
        }
    }
    
    /**
     * Test the findLongestOnesSubarray operation.
     */
    private static void testLongestOnesSubarray() {
        System.out.println("\n=== Testing Longest Ones Subarray ===");
        SlidingWindow sw = new SlidingWindow();
        
        // Test case 1: Regular array
        int[] arr1 = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
        int k1 = 2;
        int result1 = sw.findLongestOnesSubarray(arr1, k1);
        System.out.println("Longest ones subarray with at most " + k1 + " zeros in [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]: " + result1);
        if (result1 == 6) {
            System.out.println("PASS: Longest ones subarray length is 6");
        } else {
            System.out.println("FAIL: Longest ones subarray length should be 6, but got " + result1);
        }
        
        // Test case 2: All zeros
        int[] arr2 = {0, 0, 0, 0, 0};
        int k2 = 2;
        int result2 = sw.findLongestOnesSubarray(arr2, k2);
        System.out.println("Longest ones subarray with at most " + k2 + " zeros in [0, 0, 0, 0, 0]: " + result2);
        if (result2 == 2) {
            System.out.println("PASS: Longest ones subarray length is 2");
        } else {
            System.out.println("FAIL: Longest ones subarray length should be 2, but got " + result2);
        }
    }
}
