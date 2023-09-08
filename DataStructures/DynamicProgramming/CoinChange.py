"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine how many ways can you make sum B assuming you have infinite amount of each
    coin in the set.

Problem Description
You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in
the set.

NOTE:
Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).

Problem Constraints
1 <= A <= 500
1 <= A[i] <= 1000
1 <= B <= 50000

Input Format
First argument is an integer array A representing the set.
Second argument is an integer B.

Output Format
Return an integer denoting the number of ways.

Example Input
Input 1:
 A = [1, 2, 3]
 B = 4

Input 2:
 A = [10]
 B = 10

Example Output
Output 1: 4
Output 2: 1

Example Explanation
Explanation 1:
 The 4 possible ways are:
 {1, 1, 1, 1}
 {1, 1, 2}
 {2, 2}
 {1, 3}

Explanation 2:
 There is only 1 way to make sum 10.
"""


class Solution:
    # @param A : list of integers (the set of coins)
    # @param B : integer (the target sum)
    # @return an integer (number of ways to make sum B)

    def coinchange2(self, A, B):
        MOD = 1000007  # Modulus to avoid overflow

        # Initialize an array to store the number of ways to make each sum from 0 to B
        dp = [0] * (B + 1)
        dp[0] = 1  # There's one way to make sum 0 (by choosing no coins)

        # Loop through each coin in the set
        for coin in A:
            # Update the dp array from the current coin value up to B
            for j in range(coin, B + 1):
                dp[j] += dp[j - coin]  # Add the ways to make (j - coin) to the current sum j

        # Return the number of ways to make the target sum B modulo MOD
        return dp[B] % MOD


"""
# Intuition:
        # We use dynamic programming to count the number of ways to make each sum from 0 to B.
        # We start with dp[0] = 1 (one way to make sum 0) and update the dp array for each coin value.
        # For each coin, we iterate through the target sums from the coin value up to B,
        # and for each target sum, we update the number of ways to make that sum by adding the
        # number of ways to make (sum - coin) to it. Finally, we return dp[B] % MOD to avoid overflow.

TC (Time Complexity): 
The time complexity is O(A * B), where A is the number of coins in the set, and B is the target sum. This is because 
there is a nested loop that iterates through both the coin values and the target sum.

SC (Space Complexity): The space complexity is O(B) as we are using a dynamic programming array dp of size B+1 to store
 the number of ways to make each sum from 0 to B.
"""
