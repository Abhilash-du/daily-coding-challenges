class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = [0] + A
        hmap = {}
        n = len(A)
        sum = 0
        for i in range(n):
            val = A[i]
            sum += val
            if sum in hmap:
                return 1
            hmap[sum] = i
        return 0

# Approach Followed/Observation:-
# The idea is to iterate through the array, and for every element A[i],
# calculate sum of elements from 0 to i (this can simply be done as sum += arr[i]).
#
# If the current sum has been seen before, then there is a zero-sum array.
#
# Hashing is used to store the sum values so that we can quickly store sum and
# find out whether the current sum is seen before or not.
