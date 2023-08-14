"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to check if There is a Valid Partition For The Array

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:-
The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements
is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

Example 1:
Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

Example 2:
Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None for _ in range(n)]  # Memoization table to store computed results

        def solve(i):
            if i >= n:  # Base case: reached the end of the array
                return True

            result = False

            if dp[i] is not None:  # If result for this index is already computed, return it
                return dp[i]

            # Rule 1: Check for exactly 2 equal elements
            if i + 1 < n and nums[i] == nums[i + 1]:
                result |= solve(i + 2)

            # Rule 2: Check for exactly 3 equal elements
            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                result |= solve(i + 3)

            # Rule 3: Check for 3 consecutive increasing elements
            if i + 2 < n and nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                result |= solve(i + 3)

            dp[i] = result  # Memoize the result for this index
            return result

        return solve(0)


"""
Intuition:
The problem involves partitioning an array into valid subarrays. A valid subarray can consist of either 2 equal 
elements, 3 equal elements, or 3 consecutive increasing elements. 
The challenge is to determine if the given array can be partitioned in such a way.

Time Complexity (TC):
The dynamic programming approach allows us to analyze each subarray once, resulting in a linear time complexity of O(n),
 where n is the size of the input array.

Space Complexity (SC):
By leveraging memoization, we store results for subproblems, leading to a space complexity of O(n), directly 
proportional to the input size. This efficient use of memory ensures optimized performance.
"""
