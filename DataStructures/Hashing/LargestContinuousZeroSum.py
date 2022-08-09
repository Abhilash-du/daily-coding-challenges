# Problem Description
# Given an array A of N integers.
# Find the largest continuous sequence in a array which sums to zero.
#
# Problem Constraints
# 1 <= N <= 106
# -107 <= A[i] <= 107
#
# Input Format
# Single argument which is an integer array A.
#
# Output Format:  Return an array denoting the longest continuous sequence with total sum of zero.
# NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
#
# Example Input: A = [1,2,-2,4,-4]
#
# Example Output: [2,-2,4,-4]
#
# Example Explanation: [2,-2,4,-4] is the longest sequence with total sum of zero.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):

        n = len(A)
        ps = 0
        hmap_indx = {0: -1}  # hashmap to store prefix sum <prefix_sum: index>

        # value to store start index and end index with highest length 
        final_start = 1
        final_end = 0
        max_len = 0

        for i in range(0, n):
            ps += A[i]
            if ps in hmap_indx.keys():  # checking if hashmap has key present
                start = hmap_indx[ps] + 1
                end = i
                if max_len < end - start + 1:  # checking if length is highest
                    max_len = end - start + 1
                    final_start = start
                    final_end = end
            else:
                hmap_indx[ps] = i
        newA = []
        for idx in range(final_start, final_end + 1):
            newA.append(A[idx])
        return newA


# For Execution purpose
A = [1, 2, -2, 4, -4]
zero_sum_arr = Solution()
print(zero_sum_arr.lszero(A))

# approach/observation followed:-
# Creating a hashmap to store prefix sum and its index.
# if a value is repeated in prefix sum, means the sum between them is zero
# We evaluated all the possible subarrays with sum zero, and then found the longest length subarray with sum zero
# At the end we have returned the new Array by storing subarray values
