"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the number of combinations that make up the provided amount.

 Coin Change II
You are given an integer array coins representing coins of different denominations and an integer amount representing a
 total amount of money. Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000

"""
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)  # Number of different coin denominations
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        # dp[i][j] represents the number of combinations to make amount j using coins up to index i.

        def countCoins(i, curr_amount):
            if curr_amount == 0:
                return 1  # If the target amount is reached exactly, there's one valid combination
            if i >= n:
                return 0  # If no more coins are available and amount is not zero, no valid combination
            if dp[i][curr_amount] != -1:
                return dp[i][curr_amount]  # Return the cached result if available

            if curr_amount < coins[i]:
                dp[i][curr_amount] = countCoins(i + 1, curr_amount)
                return dp[i][curr_amount]

            # Two choices: Take the current coin or skip it
            take = countCoins(i, curr_amount - coins[i])  # Take the current coin
            skip = countCoins(i + 1, curr_amount)  # Skip the current coin
            dp[i][curr_amount] = take + skip  # Store the result in the cache
            return take + skip

        return countCoins(0, amount)  # Start the recursive counting from the first coin


"""
Intuition:
The problem asks us to find the number of combinations that make up a given amount using different coin denominations. 
We're allowed to use each coin type an infinite number of times. To solve this, we use dynamic programming.
 We maintain a 2D table dp, where dp[i][j] represents the number of ways to make amount j using coins up to the ith 
 denomination.

The main idea is to build the solution from smaller subproblems. 
For each coin denomination, we have two choices: either we include the coin or we skip it. 
We recursively consider both these options while updating our dp table with the number of ways to reach the desired 
amount using each combination of coins.

Time Complexity (TC):
The time complexity of the code is influenced by the number of subproblems we need to solve and the number of choices
 we have for each subproblem. In this case, we have n denominations of coins and an amount amount. For each combination
  of denomination and amount, we compute the number of ways to reach that amount. This gives us a total of n * amount 
  subproblems. For each subproblem, we do a constant amount of work.

So, the overall time complexity is O(n * amount), where n is the number of coin denominations and amount is the target 
amount.

Space Complexity (SC):
The space complexity is determined by the memory required for the dp table. It's a 2D table with dimensions (n + 1) by
 (amount + 1). Therefore, the space complexity is O(n * amount).

In addition to the dp table, the recursive function consumes space on the call stack proportional to the depth of the 
recursion. In the worst case, the depth of the recursion can be up to n (the number of coin denominations), so the 
additional space complexity due to recursion is O(n).
"""
