# Problem Description
# Given an integer array A of size N.
# Return 1 if the array can be arranged to form an arithmetic progression,
# otherwise return 0.
#
# A sequence of numbers is called an arithmetic progression if
# the difference between any two consecutive elements is the same.
#
#
# Problem Constraints
# 2 <= N <= 105
# -109 <= A[i] <= 109
#
# Input Format
# The first and only argument is an integer array A of size N.
#
# Output Format
# Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.
#
# Example Input
# Input 1:  A = [3, 5, 1]
# Input 2:  A = [2, 4, 1]
#
# Example Output
# Output 1:  1
# Output 2:  0

# Example Explanation
# Explanation 1:
#  We can reorder the elements as [1,3,5] or [5,3,1] with differences
#  2 and -2 respectively, between each consecutive elements.
# Explanation 2:
#  There is no way to reorder the elements to obtain an arithmetic progression.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        flag = 0
        diff = A[1] - A[0]
        n = len(A)
        for i in range(1, n):
            if A[i] - A[i - 1] == diff:
                flag = 1
            else:
                flag = 0
                break
        return flag


# For execution purpose:-
A = [2, 4, 1]
B = [1, 2, 3, 4, 5]
ap = Solution()
print(ap.solve(A))
print(ap.solve(B))

# Observation and Implementation logic:-
# Consider that any valid arithmetic progression will be in sorted order.
#
# Sort the array, then check if the differences of all consecutive elements are equal.
#
# Time Complexity: O(NlogN)
# Space Complexity: O(1)
