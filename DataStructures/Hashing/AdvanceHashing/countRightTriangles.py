# Problem Description
# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.
# Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.
# NOTE: The answer may be large so return the answer modulo (109 + 7).
#
# Problem Constraints
# 1 <= N <= 105
# 0 <= A[i], B[i] <= 109
#
# Input Format
# The first argument given is an integer array A.
# The second argument given is the integer array B.
#
# Output Format
# Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).
#
# Example Input
# Input 1:
#  A = [1, 1, 2]
#  B = [1, 2, 1]
#
# Input 2:
#  A = [1, 1, 2, 3, 3]
#  B = [1, 2, 1, 2, 1]
#
#
# Example Output
# Output 1:  1
# Output 2:  6
#
# Example Explanation
# Explanation 1:  All three points make a right angled triangle. So return 1.
#
# Explanation 2:
#  6 triplets which make a right angled triangle are:    (1, 1), (1, 2), (2, 2)
#                                                        (1, 1), (3, 1), (1, 2)
#                                                        (1, 1), (3, 1), (3, 2)
#                                                        (2, 1), (3, 1), (3, 2)
#                                                        (1, 1), (1, 2), (3, 2)
#                                                        (1, 2), (3, 1), (3, 2)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)

        x_hmap = {}  # hashmap to store frequency of elements in x coordinate
        y_hmap = {}  # hashmap to store frequency of elements in y coordinate

        for i in range(n):
            x = A[i]
            y = B[i]
            if x in x_hmap:
                x_hmap[x] += 1
            else:
                x_hmap[x] = 1

            if y in y_hmap:
                y_hmap[y] += 1
            else:
                y_hmap[y] = 1

        ans = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            x = A[i]
            y = B[i]
            x_count = x_hmap[x] - 1  # number of elements with x coordinate
            y_count = y_hmap[y] - 1  # number of elements with y coordinate
            ans += (x_count * y_count) % mod
        return ans

# Approach Followed/Observation
# Try fixing each point as the intersection of perpendicular and base and finding other points.
#
# Once it is fixed, for the other two points, one point will share the same x-coordinate, and the other point will
# share the same y-coordinate with the selected point.
#
# We can use a map to store the points for points sharing the same x or y coordinate.
