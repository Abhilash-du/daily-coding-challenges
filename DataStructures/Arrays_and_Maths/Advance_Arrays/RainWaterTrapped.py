# Problem Description
# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# Input Format
# First and only argument is the vector A
#
# Output Format
# Return one integer, the answer to the question
#
# Example Input
# Input 1: A = [0, 1, 0, 2]
# Input 2: A = [1, 2]
#
# Example Output
# Output 1: 1
# Output 2: 0
#
# Example Explanation
# Explanation 1: 1 unit is trapped on top of the 3rd element.
# Explanation 2: No water is trapped.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        # step1: we will create prefix max and suffix max
        preA = [A[0]]
        for i in range(1, n):
            val = max(preA[i - 1], A[i])
            preA.append(val)  # prefix max

        suffA = [A[n - 1]]
        for i in range(n - 2, -1, -1):
            val = max(A[i], suffA[n - i - 2])
            suffA.append(val)  # suffix max
        suffA = suffA[::-1]

        # step2: we will check for left max and right max for each index
        final_val = 0
        for i in range(1, n - 1):
            left = preA[i - 1]  # max element from left
            right = suffA[i + 1]  # max element from right
            index_val = max(0, min(left, right) - A[i])  # to find water tapped at each index
            final_val = final_val + index_val
        return final_val

# Approach followed:-
# We can keep 2 arrays ‘pre’ and ‘suf’. pre[i] is the maximum height for all i from 0 to i and suf[i]
# is the maximum height for all i from i to n-1.
# Now for each i from 1 to n-2 (as no water can be stored at indexes 0 and 1) just add the maximum amount water
# that can be stored. The maximum amount of water that can be stored is the minimum of(max height towards left
# of i,max height towards right of i)-A[i]
# i.e. min(pre[i-1],suf[i+1])-A[i]. But if min(pre[i-1],suf[i+1])-A[i]<0 we don't add anything. (i.e we add 0)
#
# Time Complexity : O(n)
# Auxiliary Space : O(n)
