# Problem Description You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2,
# ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the
# characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.
#
# Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
#
# If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements
# denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
#
# NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
#
#
#
# Problem Constraints
# 1 <= size of string <= 100000
#
#
#
# Input Format
# First and only argument is a string A.
#
#
#
# Output Format
# Return an array of integers denoting the answer.
#
#
#
# Example Input
# Input 1:
#
# A = "010"
# Input 2:
#
# A = "111"
#
#
# Example Output
# Output 1:
#
# [1, 1]
# Output 2:
#
# []
#
#
# Example Explanation
# Explanation 1:
#
# A = "010"
#
# Pair of [L, R] | Final string
# _______________|_____________
# [1 1]          | "110"
# [1 2]          | "100"
# [1 3]          | "101"
# [2 2]          | "000"
# [2 3]          | "001"
#
# We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
# Explanation 2:
#
# No operation can give us more than three 1s in final string. So, we return empty array [].
#
#
#
# See Expected Output

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if "0" not in A:
            return []

        left = 0
        n = len(A)
        count = 0
        max_count = 0
        ans = [0, 0]

        for i in range(n):
            # iterate through array
            if A[i] == "0":
                # if value is 0 increment counter
                count += 1
                if max_count < count:
                    # if this is maximum count update final values
                    ans[0] = left + 1
                    ans[1] = i + 1
                    max_count = count
            else:
                count -= 1
                if count < 0:
                    # count is less than zero then reset count
                    count = 0
                    left = i + 1
        return ans

# Approach Followed/Observation:-
# Note the net change in the number of 1s in string S when we flip bits of string S.
# Say it has A 0s and B 1s. Eventually, there are B 0s and A 1s.
#
# So, the number of 1s increased by A - B. We want to choose a sub-array that maximizes this.
# Note that if we change 1s to -1, the sum of values will give us A - B. Then, we have to find a sub-array
# with the maximum sum, which can be done via Kadane’s Algorithm.
