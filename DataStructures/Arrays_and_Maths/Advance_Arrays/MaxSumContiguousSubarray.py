# Problem Description
# Find the contiguous non-empty sub-array within an array, A of length N, with the largest sum.
#
# Problem Constraints
# 1 <= N <= 1e6
# -1000 <= A[i] <= 1000
#
# Input Format
# The first and the only argument contains an integer array, A.
#
# Output Format
# Return an integer representing the maximum possible sum of the contiguous sub-array.
#
# Example Input
# Input 1: A = [1, 2, 3, 4, -10]
# Input 2: A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# Example Output
# Output 1:  10
# Output 2:  6
#
# Example Explanation
# Explanation 1:  The sub-array [1, 2, 3, 4] has the maximum possible sum of 10.
# Explanation 2:  The sub-array [4,-1,2,1] has the maximum possible sum of 6.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        ans = -10 ** 7 + 3
        curr_sum = 0
        for i in range(n):
            curr_sum += A[i]
            ans = max(curr_sum, ans)
            if curr_sum < 0:
                curr_sum = 0
        return ans

# Solution Approach:- (Kadane's Algorithm)
# Let us say Ai, Ai+1 … Aj is our optimal solution.
#
# Note that no prefix of the solution will ever have a negative sum.
#
# Let us say Ai … Ak prefix had a negative sum.
#
# Sum ( Ai Ai+1 … Aj ) = Sum (Ai … Ak) + Sum(Ak+1 … Aj)
#
# Sum ( Ai Ai+1 … Aj) - Sum(Ak+1 … Aj) = Sum(Ai … Ak)
#
# Now, since Sum(Ai … Ak) < 0,
#
# Sum (Ai Ai+1 … Aj) - Sum (Ak+1 … Aj) < 0
#
# which means Sum(Ak+1 … Aj ) > Sum (Ai Ai+1 … Aj)
#
# This contradicts the fact that Ai, Ai+1 … Aj is our optimal solution.
#
# Instead, Ak+1, Ak+2 … Aj will be our optimal solution.
#
# Similarly, you can prove that it is always good to include a prefix with a positive sum for the optimal solution.
#
# Try to come up with a solution based on the previous 2 facts.
#
# Here’s one Approach.
# Keep two variables ‘curSum’ and ‘maxSum’ which denotes the current sum ending at the given position and the maximum sum of a subarray respectively.
# Iterate through the array , at every index we will add the current element to our curSum , after this we can update the maxSum as max(maxSum,curSum), After this we can just check if curSum is less than 0 , if it is then just replace curSum with 0.
#
# Time Complexity : O(n)
# Space Complexity(extra) : O(1)