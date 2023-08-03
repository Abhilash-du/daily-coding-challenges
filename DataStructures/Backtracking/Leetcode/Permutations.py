"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine all the possible permutations

46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []  # Store the final list of permutations

        def backtrack(curr_permutation):
            if len(curr_permutation) == n:
                # If the current permutation has reached the desired length, add it to the result list
                result.append(curr_permutation[:])  # Use a copy of the current permutation to avoid reference issues
                return

            for num in nums:
                if num not in curr_permutation:
                    curr_permutation.append(num)  # Choose the next element for the permutation
                    backtrack(curr_permutation)  # Recursively generate permutations with the current choice
                    curr_permutation.pop()  # Backtrack by removing the last element for the next iteration

        backtrack([])  # Start with an empty permutation to generate all permutations
        return result


"""
# Intuition:
 To generate all permutations, we use backtracking.
 We start with an empty permutation and explore all possible choices for the next element.
 When the permutation reaches the desired length, it's added to the result.
 Otherwise, we continue exploring different choices until all permutations are found.

# Time Complexity (TC):
 The time complexity of our solution is O(N!), where N is the length of the input list.
 This is because there are N! permutations of a list with N elements, and our algorithm examines all of them.

# Space Complexity (SC):
 The space complexity of our solution is O(N) for the recursion stack, where N is the length of the input list.
 The result list also contributes to space, but it is not counted in the space complexity analysis.
The added comments now provide the Intuition behind the algorithm, as well as the Time 
"""