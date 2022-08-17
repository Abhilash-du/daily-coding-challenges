# Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
# Find and return the length of the longest consecutive 1’s that can be achieved.
#
# Input Format: The only argument given is string A.
# Output Format: Return the length of the longest consecutive 1’s that can be achieved.
#
# Constraints: 1 <= length of string <= 1000000
# A contains only characters 0 and 1.
#
# For Example
#
# Input 1:  A = "111000"
# Output 1:   3
#
# Input 2:   A = "111011101"
# Output 2:     7

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if "1" not in A:
            return 0
        n = len(A)
        s = -1
        e = 0
        last_zero = -1
        max_len = 0
        ones_count = 0
        first_flag = True
        while e < n:
            if A[e] == "1":  # counting ones in order to check if there is access 1s, at the end
                ones_count += 1
            if first_flag is True and A[e] == "1":  # checking for first 1 in string
                s = e
                first_flag = False
            if A[e] == "0":
                s = last_zero + 1  # updating the start index
                last_zero = e  # current index as the last zero found
            max_len = max(max_len, e - s + 1)
            e = e + 1
        if max_len > ones_count:
            return max_len - 1
        else:
            return max_len


# Approach followed:-
# Firstly checking for the start index with one(example 00100, from 2nd index we have to start checking for further one)
# within each loop we will be storing position of last zero seen
# so that we can ignore the first zero and count the overall ones. (kind of like sliding window approach,
# but expanding from one side)
# after going through all indexes, we have got the max_length with highest consicutive ones (with swap)
# incase the total max_length is greater than ones count, means we cant swap, so we will have to decrement one index
# count
