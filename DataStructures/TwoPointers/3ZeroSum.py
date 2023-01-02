# Problem Description
#
# Given an array A of N integers, are there elements a, b, c in S such that a + b + c = 0
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order.
# (ie, a ≤ b ≤ c) The solution set must not contain duplicate triplets.
#
#  Problem Constraints
#  0 <= N <= 7000
#  -108 <= A[i] <= 108
#
# Input Format
#  Single argument representing a 1-D array A.
#
# Output Format
#  Output a 2-D vector where each row represent a unique triplet.
#
# Example Input
#  A = [-1,0,1,2,-1,4]
#
# Example Output
#
# [ [-1,0,1],
#   [-1,-1,2] ]
#
#
# Example Explanation
# Out of all the possible triplets having total sum zero,only the above two triplets are unique.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A = sorted(A)
        ans = []
        n = len(A)
        for i in range(len(A) - 2):
            # to avoid duplicate triplet
            if i > 0 and A[i] == A[i - 1]:
                continue
            j = i + 1
            k = len(A) - 1
            target = -(A[i])
            while j < k:
                cur_sum = A[j] + A[k]
                if cur_sum == target:
                    ans.append([-target, A[j], A[k]])
                    # another conditional for not calculating duplicates
                    while j < k and A[j] == A[j + 1]:
                        j += 1
                    while j < k and A[k] == A[k - 1]:
                        k -= 1
                    j = j + 1
                    k = k - 1
                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1
        return ans

# Solution Approach/ Observation:-
# Getting a Time Limit exceeded or Output Limit exceeded?
# Make sure you handle case of empty input [].
# In C++/C, usually if you run a loop till array.size() - 2,
# it can lead to the program running indefinitely as array.size() is unsigned int,
# and the subtraction just makes it wrap over to a big integer.
# Make sure you are not processing the same triplets again.
#
# Skip over the duplicates in the array.
#
# Try a input like :
# -1 -1 -1 -1 0 0 0 0 1 1 1 1
# Ideally, you should get only 2 pairs : {[-1 0 1], [0 0 0]}
