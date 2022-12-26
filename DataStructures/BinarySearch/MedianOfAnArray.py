# Problem Description
# There are two sorted arrays A and B of sizes N and M respectively.
# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
#
# NOTE:
# The overall run time complexity should be O(log(m+n)).
# IF the number of elements in the merged array is even, then the median is the average of (n/2)th
# and (n/2+1)th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.
#
# Problem Constraints
# 1 <= N + M <= 2*10^6
#
# Input Format
# The first argument is an integer array A of size N.
# The second argument is an integer array B of size M.
#
# Output Format
# Return a decimal value denoting the median of two sorted arrays.
#
# Example Input
# Input 1:
#  A = [1, 4, 5]
#  B = [2, 3]
# Input 2:
#  A = [1, 2, 3]
#  B = [4]
#
# Example Output
# Output 1:  3.0
# Output 2:  2.5
#
# Example Explanation
# Explanation 1:  The median of both the sorted arrays will be 3.0.
# Explanation 2:  The median of both the sorted arrays will be (2+3)/2 = 2.5.
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        half = total // 2
        if len(A) < len(B):
            A, B = B, A

        l = 0
        r = len(B) - 1

        while True:
            midB = (l + r) // 2
            midA = half - midB - 2

            BLeft = B[midB] if midB >= 0 else float("-infinity")
            BRight = B[midB + 1] if midB < len(B) - 1 else float("infinity")
            ALeft = A[midA] if midA >= 0 else float("-infinity")
            ARight = A[midA + 1] if midA < len(A) - 1 else float("infinity")

            if ALeft <= BRight and ARight >= BLeft:
                if total % 2 == 0:
                    val = (min(ARight, BRight) + max(ALeft, BLeft)) / 2
                else:
                    val = min(ARight, BRight)
                return val
            elif BLeft > ARight:
                r = midB - 1
            else:
                l = midB + 1

# Solution Approach/Observation:-
# Given a sorted array A of length m, we can split it into two parts:
#
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All the elements in the right part are greater than those in the left part.
#
# The left part has “i” elements, and the right has “m - i” elements.
#
# There are “m + 1” kinds of splits. (i = 0 ~ m)
#
# When i = 0, the left part has “0” elements, right part has “m” elements.
#
# When i = m, the left part has “m” elements, right part has “0” elements.
#
# For array B, we can split it with the same way:
#
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and the right has “n - j” elements.
#
# Put A’s left part and B’s left part into one set. (Let us name this set “LeftPart”)
#
# Put A’s right part and B’s right part into one set. (Let us name this set”RightPart”)
#
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
#
# 1) LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
#
# 2) All elements in RightPart is greater than elements in LeftPart,
#
# Then we split all elements in {A, B} into two parts with equal length, and one part is always greater than the
# other part.
#
# Then the median can be easily found.
#
# The expected time complexity gives away binary search in this case.
# We will do binary search for the answer in this case.
#
# Given a sorted array A of length m, we can split it into two parts:
#
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All elements in the right part are greater than elements in the left part.
#
# The left part has i elements, and the right has m - i elements.
# There are m + 1 kinds of splits.
#
# (i = 0 ~ m)
#
# When i = 0, the left part has “0” elements, the right part has “m” elements.
# When i = m, the left part has “m” elements, right part has “0” elements.
#
# For the array B, we can split it in the same way:
#
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and the right part has “n - j” elements.
#
# Put A’s left part and B’s left part into one set. (Let’s name this set “LeftPart”)
#
# Put A’s right part and B’s right part into one set. (Let’s name this set”RightPart”)
#
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
#
# LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
# All elements in RightPart is greater than
# elements in LeftPart, Then we can split all elements in {A, B} into two parts with equal length, and one part is
# always greater than the other part.
#
# Then the median can thus be easily found.
#
# To ensure these two conditions, we need to ensure:
#
# Condition 1 :
#  i + j == (m - i) + (n - j)
#  OR i + j == (m - i) + (n - j) + 1
# This means if n >= m,
#
# i = 0 to m
# j = (m + n + 1) / 2 - i
# Condition 2
#  B[j - 1] <= A[i] and A[i - 1] <= B[j]
# Considering edge values, we need to ensure:
#
#    (j == 0 or i == m or B[j - 1] <= A[i]) and
#
#    (i == 0 or j == n or A[i - 1] <= B[j])
# So, all we need to do is:
#
# Search i from 0 to m to find an object i to meet conditions (1) and (2) above.
# And we can do this search by binary search.
#
# How?
#
# If B[j0 - 1] > A[i0], than the object ix can’t be in [0, i0].
#
# Why?
#
# Because if
#
#   ix < i0,
#   => jx = (m + n + 1) / 2 - ix > j0
#   => B[jx - 1] >= B[j0 - 1] > A[i0] >= A[ix].
# This violates the condition (2). So ix can’t be less than i0.
#
# And if A[i0 - 1] > B[j0], than the object ix can’t be in [i0, m].
# So we can do the binary search following the steps described below:
#
# set imin, imax = 0, m, then start searching in [imin, imax]
# Search in [imin, imax]:
#     i = (imin + imax) / 2
#     j = ((m + n + 1) / 2) - i
#     if B[j - 1] > A[i]:
#         search in [i + 1, imax]
#     else if A[i - 1] > B[j]:
#         search in [imin, i - 1]
#     else:
#         if m + n is odd:
#             answer is max(A[i - 1], B[j - 1])
#         else:
#             answer is (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2
