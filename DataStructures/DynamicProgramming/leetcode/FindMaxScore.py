"""
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

Constraints:
1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 10^6

"""


import math
import collections


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = collections.defaultdict(int)
        return self.findMaxScore(nums, 1, 0, dp)

    def findMaxScore(self, nums, op, mask, dp):
        n = len(nums)
        if mask in dp:
            return dp[mask]

        max_score = 0
        # Iterate over all possible pairs of indices (i, j) where i < j
        for i in range(n - 1):
            if (1 << i) & mask: continue  # If the i-th bit is set in the mask, skip to the next iteration
            for j in range(i + 1, n):
                if (1 << j) & mask: continue  # If the j-th bit is set in the mask, skip to the next iteration

                new_mask = mask | (1 << i) | (1 << j)  # Update the mask to include the i-th and j-th bits

                curr_score = op * math.gcd(nums[i], nums[j])  # Calculate the current score for the pair (i, j)
                remaining_score = self.findMaxScore(nums, op + 1, new_mask,
                                                    dp)  # Recursively calculate the score for the remaining pairs
                dp[mask] = max(dp[mask], curr_score + remaining_score)  # Update the maximum score for the current mask

        return dp[mask]

"""
Approach Followed
Approach:

1. The maxScore function serves as a wrapper function that initializes the dynamic programming (DP) dictionary (dp) and 
    calls the findMaxScore function to compute the maximum score.
2. The findMaxScore function is a recursive function that takes four parameters: nums (the input array), 
    op (the operation count), mask (a bitmask representing the selected elements), 
    and dp (the DP dictionary to store previously computed results).
3. The base case of the recursion is when the current bitmask (mask) is already present in the DP dictionary (dp), 
    in which case the corresponding maximum score is returned.
4. The function iterates over all possible pairs of indices (i, j) in the input array (nums) where i < j. It checks if 
    the i-th and j-th bits are set in the bitmask (mask). If either of them is set, it skips to the next iteration, 
    as those elements are already included in the current bitmask.
5. For each valid pair (i, j), it calculates a new bitmask (new_mask) by setting the i-th and j-th bits 
    in the current mask.
6. It calculates the current score (curr_score) for the pair (i, j) by multiplying the operation count (op) with 
the greatest common divisor (GCD) of the corresponding elements in the array (nums[i] and nums[j]).
7 .It recursively calls the findMaxScore function with the updated bitmask (new_mask), incremented operation 
count (op+1), and the same input array (nums).
8. The result of the recursive call (remaining_score) represents the maximum score that can be obtained from the
 remaining pairs in the array.
9. Finally, the maximum score for the current bitmask (dp[mask]) is updated by taking the maximum of the current score
 (curr_score) plus the remaining score (remaining_score).
10. The maximum score for the current bitmask is stored in the DP dictionary (dp) for future reference and returned
 as the result.
 
 
Time Complexity (TC): O(2^N * N^2 * log min(nums[i], nums[j]))
The outer loop iterates over 2^N possible bitmasks.
The nested loops iterate over N^2 possible pairs of indices (i, j).
The GCD calculation between nums[i] and nums[j] has a time complexity of log min(nums[i], nums[j]).

Space Complexity (SC): O(2^N)
The space complexity is dominated by the DP dictionary (dp) used to store maximum scores for different bitmasks.
Since there are 2^N possible bitmasks, the space complexity is O(2^N).

Please note that the TC and SC calculations assume that the GCD calculation (math.gcd) takes constant time.
 The actual time complexity may vary depending on the specific implementation of the GCD algorithm used in the
  math library.
"""
