# Problem Description
#
# The demons had captured the princess and imprisoned her in the bottom-right corner of a
# dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in
# the top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to
# 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in
# each step.
#
# Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is
# able to rescue the princess.
#
#
#
# Problem Constraints
# 1 <= M, N <= 500
# -100 <= A[i] <= 100
#
# Input Format
# First and only argument is a 2D integer array A denoting the grid of size M x N.
#
# Output Format
# Return an integer denoting the knight's minimum initial health so that he is able to rescue the princess.
#
# Example Input
# Input 1:
#
#  A = [
#        [-2, -3, 3],
#        [-5, -10, 1],
#        [10, 30, -5]
#      ]
# Input 2:
#  A = [
#        [1, -1, 0],
#        [-1, 1, -1],
#        [1, 0, -1]
#      ]
#
# Example Output
# Output 1:  7
# Output 2:  1
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        r = len(A) - 1
        c = len(A[0]) - 1
        dp = [[-1 for _ in range(c + 1)] for __ in range(r + 1)]

        # minimum value that should be there at the end to find princess
        if A[r][c] < 0:
            dp[r][c] = abs(A[r][c]) + 1
        else:
            dp[r][c] = 1

        for i in range(c + 1):
            row = c - i
            for j in range(r + 1):
                col = r - j
                # for element at end
                if row == r and col == c:
                    dp[row][col] = max(1 - A[row][col], 1)
                    continue
                # for last column
                if col == c:
                    dp[row][col] = max(dp[row + 1][col] - A[row][col], 1)
                    continue
                # for last row
                if row == r:
                    dp[row][col] = max(dp[row][col + 1] - A[row][col], 1)
                    continue
                    # for other elements
                dp[row][col] = max(min(dp[row][col + 1], dp[row + 1][col]) - A[row][col], 1)
        return dp[0][0]

# Solution Approach:-
# There are only 2 positions you can directly go to from i, j. (i+1, j) and (i, j + 1).
#
# So if you knew the optimal path requirements for (i + 1, j) and (i, j + 1),
# you could choose the minimum of the two and be done with it.
#
# Build the dp array, start from the bottom right corner ,
# let’s say hp[i][j] represents the min health point needed at position (i, j).
#
# So, hp[i][j] = max(1, min(hp[i][j+1], hp[i+1][j]) - dungeon[i][j])
#
# The final answer value is stored at hp[0][0].
