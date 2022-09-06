# Problem Description
# You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the
# cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees
# (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
# The cost of these trees is Bp + Bq + Br.
#
# You are to choose 3 trees such that their total cost is minimum. Return that cost.
# If it is not possible to choose 3 such trees return -1.
#
# Problem Constraints
# 1 <= A[i], B[i] <= 109
# 3 <= size(A) = size(B) <= 3000
#
# Input Format
# First argument is an integer array A.
# Second argument is an integer array B.
#
# Output Format
# Return an integer denoting the minimum cost of choosing 3 trees whose heights are strictly in increasing order,
# if not possible, -1.
#
# Example Input
# Input 1:
#  A = [1, 3, 5]
#  B = [1, 2, 3]
#
# Input 2:
#  A = [1, 6, 4, 2, 6, 9]
#  B = [2, 5, 7, 3, 2, 7]
#
# Example Output
# Output 1: 6
# Output 2: 7
#
# Example Explanation
# Explanation 1:  We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6.
# Explanation 2:  We can choose the trees with indices 1, 4 and 5, and the cost is 2 + 3 + 2 = 7.
#  This is the minimum cost that we can get.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, arr, cost):
        n = len(arr)
        ans = 10 ** 9 + 7
        for i in range(n):
            curr_val = arr[i]
            left_min = 10 ** 9 + 7
            right_min = 10 ** 9 + 7

            # find left min
            for j in range(i):
                if arr[j] < curr_val:
                    left_min = min(left_min, cost[j])

            # find right max
            for k in range(i + 1, n):
                if arr[k] > curr_val:
                    right_min = min(right_min, cost[k])

            # check if its minimum
            if left_min != 10 ** 9 + 7 and right_min != -10 ** 9 + 7:
                final_cost = left_min + right_min + cost[i]
                ans = min(ans, final_cost)
        if ans == 10 ** 9 + 7:
            return -1
        return ans

# Approach Followed:-
#  fix the middle element and search for the smaller element with minimum cost on its left and the
#  larger element with minimum cost on its right in the given array. If a valid triplet is found then
#  update the minimum cost far. The time complexity of this approach will be O(n2).
