"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to Predict the Winner

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0.
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
which reduces the size of the array by 1. The player adds the chosen number to their score.
The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner,
and you should also return true. You may assume that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True  # If there's only one element, Player 1 is the winner

        # Initialize a 2D DP array to store the scores of both players in each subgame
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def player1Score(start, end):
            # This recursive function calculates the maximum score that Player 1 can achieve from the subarray
            # nums[start:end+1].
            if start > end:
                return 0  # If the subarray is empty, the score is 0.
            if start == end:
                return nums[start]  # If there's only one element in the subarray, return its value.
            if dp[start][end] != -1:
                return dp[start][end]  # If the score for this subgame has already been calculated, return it.

            # Player 1 can choose from either end of the subarray, and Player 2 will respond optimally.
            # We calculate the scores for both choices and take the maximum.
            take_s = nums[start] + min(player1Score(start + 2, end), player1Score(start + 1, end - 1))
            take_e = nums[end] + min(player1Score(start, end - 2), player1Score(start + 1, end - 1))
            dp[start][end] = max(take_s, take_e)  # Store the maximum score for this subgame in the DP array.
            return dp[start][end]

        totalScore = sum(nums)  # Calculate the total sum of all elements in the array.
        p1 = player1Score(0, n - 1)  # Calculate the maximum score that Player 1 can achieve from the whole array.
        p2 = totalScore - p1  # Calculate the score of Player 2 by subtracting Player 1's score from the total score.
        return p1 >= p2  # If Player 1's score is greater than or equal to Player 2's score, return True
        # (Player 1 wins).


"""
Intuition:
The problem can be solved using dynamic programming. The goal is to find the maximum score that Player 1 can achieve by
 optimally selecting numbers from either end of the array, while Player 2 responds optimally as well. To do this, 
 we use a recursive approach with memoization (dynamic programming) to avoid redundant calculations.

Time Complexity:
The time complexity of the algorithm is O(N^2), where N is the number of elements in the input array nums. 
This is because we have a nested recursive function that can be called for O(N^2) different subarrays, and each 
recursive call performs constant-time operations.

Space Complexity:
The space complexity of the algorithm is O(N^2), which comes from the space used to store the dp table. 
It has dimensions NxN to store the scores for all possible subarrays of nums. Additionally, the recursive function uses
 the call stack, which can have a maximum depth of N due to the recursive nature of the algorithm. 
 Hence, the overall space complexity is O(N^2).
"""