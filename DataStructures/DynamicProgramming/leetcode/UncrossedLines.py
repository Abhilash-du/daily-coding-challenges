"""
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

Example1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4
 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000

"""


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # get the length of both lists
        n = len(nums1)
        m = len(nums2)
        # initialize a 2D array with -1 to store the results of subproblems
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        # call the helper function to find the maximum number of uncrossed lines
        return self.countUncrossedLines(nums1, nums2, 0, 0, dp)

    def countUncrossedLines(self, nums1, nums2, i, j, dp):
        # base case: if either of the lists is empty, then no uncrossed lines are possible
        if i == len(nums1) or j == len(nums2):
            return 0

        # if we have already solved this sub-problem, then return the saved result
        if dp[i][j] != -1:
            return dp[i][j]

        count = 0
        # if the current elements of both lists match, then we can draw a line between them
        if nums1[i] == nums2[j]:
            count = 1 + self.countUncrossedLines(nums1, nums2, i + 1, j + 1, dp)
        else:
            # if the current elements do not match, then we can either skip the current element in nums1
            # or skip the current element in nums2, and take the maximum of these two options
            nums1_count = self.countUncrossedLines(nums1, nums2, i + 1, j, dp)
            nums2_count = self.countUncrossedLines(nums1, nums2, i, j + 1, dp)
            count = max(nums1_count, nums2_count)

        # save the result of this sub-problem to the dp array
        dp[i][j] = count
        return dp[i][j]

"""
Approach Followed:-
The given code uses dynamic programming to solve the problem. It defines a recursive function countUncrossedLines 
that calculates the maximum number of uncrossed lines that can be drawn between two given subarrays of nums1 and 
nums2. The function takes four arguments: the two subarrays nums1[i:] and nums2[j:], and the indices i and j 
indicating the starting positions of the subarrays.


The function first checks if either of the subarrays is empty. If so, it returns 0, since no uncrossed lines can be 
drawn between empty subarrays.

If the current subproblems has already been solved before, the function returns the saved result to avoid recomputing 
the same subproblem.

If the current elements of both subarrays match, the function adds 1 to the result of the recursive call with the 
next elements in both subarrays. This is because a connecting line can be drawn between the current elements.

If the current elements do not match, the function tries to skip the current element in either nums1 or nums2, 
and takes the maximum of the resulting counts. This is because the current element cannot be part of any connecting 
line.

Finally, the result of the current subproblem is saved to the dp array, and returned.

The main function maxUncrossedLines initializes the dp array and calls the countUncrossedLines function with the 
entire nums1 and nums2 arrays.

Time Complexity:

The time complexity of the code is O(mn), where m and n are the lengths of the input arrays nums1 and nums2. This is 
because the code solves mn subproblems, each of which takes O(1) time. Space Complexity:

The space complexity of the code is O(m*n), which is the size of the dp array used to store the results 
of the sub-problems.
"""
