# Problem Description
# Given an integer array A containing N distinct integers.
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
#
# NOTE: Pair (a, b) and (b, a) is considered to be the same and should be counted once.
#
#
# Problem Constraints
# 1 <= N <= 10^5
# 1 <= A[i], B <= 10^7
#
# Input Format
# The first argument is an integer array A.
# The second argument is an integer B.
#
# Output Format
# Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.
#
# Example Input
# Input 1:
#  A = [5, 4, 10, 15, 7, 6]
#  B = 5
#
# Input 2:
#  A = [3, 6, 8, 10, 15, 50]
#  B = 5
#
#
# Example Output
# Output 1: 1
# Output 2: 2
#
# Example Explanation
# Explanation 1: (10 ^ 15) = 5
# Explanation 2: (3 ^ 6) = 5 and (10 ^ 15) = 5

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        hmap = {}
        count = 0
        for i in range(n):
            val = A[i] ^ B
            if val in hmap.keys():
                count += 1
            hmap[A[i]] = i
        return count

# Observation/Approach Followed:-
# A Simple solution is to traverse each element and check if there’s another number whose XOR with it is equal to B.
# This solution takes O(N2) time.
#
# The efficient solution to this problem takes O(N) time.
# The idea is based on the fact that A[i] ^ A[j] is equal to B if and only if A[i] ^ B is equal to A[j].
#
# 1. Initialize the result as 0.
# 2. Create an empty dictionary “hmap”.
# 3. Do the following for each element A[i] in A[]
#       1. If B ^ A[i] is in “hmap”, then increment the result by 1.
#       2.Insert A[i] into the hash set “hmap”.
#  4. Return result.
