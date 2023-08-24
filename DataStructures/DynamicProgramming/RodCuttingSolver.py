# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the e maximum value that can be obtained by cutting up the rod and
#                selling the pieces.
"""
Q2. Cutting a Rod
Problem Description
Given a rod of length N units and an array A of size N denotes prices that contains prices of all pieces of size 1 to N.
Find and return the maximum value that can be obtained by cutting up the rod and selling the pieces.

Problem Constraints
1 <= N <= 1000
0 <= A[i] <= 10^6

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the maximum value that can be obtained by cutting up the rod and selling the pieces.

Example Input
Input 1: A = [3, 4, 1, 6, 2]
Input 2: A = [1, 5, 2, 5, 6]

Example Output
Output 1: 15
Output 2: 11

Example Explanation
Explanation 1: Cut the rod of length 5 into 5 rods of length (1, 1, 1, 1, 1) and sell them for (3 + 3 + 3 + 3 + 3) = 15.
Explanation 2: Cut the rod of length 5 into 3 rods of length (2, 2, 1) and sell them for (5 + 5 + 1) = 11.
"""


class RodCuttingSolver:
    # A utility function that calculates the maximum value obtainable
    # by cutting up the rod of length 'units' using prices from array 'prices'
    def maxObtainableValue(self, prices, units, dp):
        if units == 0:
            return 0

        # If the result for 'units' is already computed, return it
        if dp[units] != -1:
            return dp[units]

        max_value = 0
        # Try all possible cuts and find the one that yields maximum value
        for cut_size in range(1, units + 1):
            # Calculate the value for the current cut and recursively explore other cuts
            current_value = prices[cut_size - 1] + self.maxObtainableValue(prices, units - cut_size, dp)
            max_value = max(max_value, current_value)

        # Store the computed value in the DP array and return it
        dp[units] = max_value
        return max_value

    def solveRodCutting(self, prices):
        n = len(prices)
        # Initialize a DP array to store computed results for subproblems
        dp = [-1] * (n + 1)

        # Call the utility function to calculate the maximum obtainable value
        max_value = self.maxObtainableValue(prices, n, dp)
        return max_value


"""
Intuition:
The rod cutting problem can be solved using dynamic programming.
The idea is to consider all possible cuts and recursively calculate
the maximum obtainable value for each possible cut. We use a DP array
to store the results of subproblems, avoiding redundant calculations.

Time Complexity:
The time complexity of this solution is O(n^2), where n is the length of the rod.
For each possible cut size, we perform constant time operations, and we consider
all possible cut sizes up to n.

Space Complexity:
The space complexity is O(n), where n is the length of the rod. This is due to the
space used by the DP array to store results of subproblems.
"""
