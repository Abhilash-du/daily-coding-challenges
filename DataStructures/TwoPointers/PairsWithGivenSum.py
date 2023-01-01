# Problem Description
# Given a sorted array of integers (not necessarily distinct) A and an integer B,
# find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
#
# Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).
#
# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9
#
# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.
#
# Output Format
# Return the number of pairs for which sum is equal to B modulo (10^9+7).
#
# Example Output:-
# Output 1:  3
# Output 2:  1
#
# Example Explanation
# Explanation 1:
#  Any two pairs sum up to 2.
# Explanation 2:
#  only pair (1, 2) sums up to 2.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        i = 0
        j = n - 1
        ans = 0
        while i < j:
            sum_val = A[i] + A[j]
            if sum_val < B:
                i += 1
            elif sum_val > B:
                j -= 1
            else:
                if A[i] == A[j]:
                    # for same element in the middle: 1111
                    ele_len = j - i + 1
                    totalPairs = (ele_len * (ele_len - 1)) // 2
                    ans += totalPairs
                    break
                else:
                    # for elements like 1122
                    dup1 = 1
                    i += 1
                    while A[i] == A[i - 1]:
                        i += 1
                        dup1 += 1
                    dup2 = 1
                    j -= 1
                    while A[j + 1] == A[j]:
                        j -= 1
                        dup2 += 1
                    ans += dup1 * dup2
        return ans % ((10 ** 9) + 7)

# Solution Approach/ Observation:-
# Let us formulate a two pointer approach to the this problem.
# We will first sort the given array and use two pointers i and j with i = 0, j = Length of Array - 1.
# We will have three conditions:
#
# 1. A[i] + A[j] < sum  --> We will increase the pointer i.
# 2. A[i] + A[j] > sum  --> We will decrease the pointer j.
# 3. A[i] + A[j] = sum  --> We will count the frequency of A[i] and A[j] and multiply them and add to the answer.
# Note, that if A[i] and A[j] are equal in value, then we will have to change the formula instead:
# freq(A[i]) * freq(A[i]) –> freq(A[i]) * (freq(A[i]) - 1) / 2
# to avoid overhunting pairs.
#
# Refer to the complete solution for more details.
