"""
Q1. 0-1 Knapsack
Problem Description
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Problem Constraints
1 <= N <= 10^3
1 <= C <= 10^3
1 <= A[i], B[i] <= 10^3

Input Format:
First argument is an integer array A of size N denoting the values on N items.
Second argument is an integer array B of size N denoting the weights on N items.
Third argument is an integer C denoting the knapsack capacity.

Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller
than or equal to C.

Example Input
Input 1:
 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50

Input 2:
 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10

Example Output
Output 1: 220
Output 2: 0


Example Explanation:-
Explanation 1:
 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220

Explanation 2:
 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack
 therefore answer is 0.

"""
class Solution:
    def recursiveKnapsack(self, Values, Weights, W):
        """
        Recursive Solution for the Knapsack Problem.

        Intuition:
        - The recursive approach explores two choices for each item: including it or excluding it from the knapsack.
        - By considering all items, we can determine the maximum value subset within the given capacity.

        Time Complexity (TC):
        - The time complexity is exponential, O(2^N), where N is the number of items.
        - The number of function calls grows exponentially with the input size.

        Space Complexity (SC):
        - The space complexity is O(N), where N is the number of items.
        - It is determined by the maximum recursion depth.
        """

        def knapsackRecursive(i, W):
            # Base case: No items left or knapsack capacity is zero
            if i == 0 or W == 0:
                return 0

            # If the weight of the current item is more than the remaining capacity 'W'
            # Exclude the item and recursively solve for the remaining items
            if Weights[i - 1] > W:
                return knapsackRecursive(i - 1, W)

            # Choose the maximum value between including the current item and excluding the current item
            included = Values[i - 1] + knapsackRecursive(i - 1, W - Weights[i - 1])
            excluded = knapsackRecursive(i - 1, W)

            return max(included, excluded)

        return knapsackRecursive(len(Values), W)

    def dynamicProgrammingKnapsack(self, Values, Weights, W):
        """
        Dynamic Programming Solution for the Knapsack Problem.

        Intuition:
        - The dynamic programming approach uses a 2D array to store and reuse intermediate results.
        - It iteratively calculates the maximum value for each item and capacity combination.

        Time Complexity (TC):
        - The time complexity is O(N * C), where N is the number of items and C is the knapsack capacity.
        - It performs calculations for each item and capacity combination once.

        Space Complexity (SC):
        - The space complexity is O(N * C), where N is the number of items and C is the knapsack capacity.
        - It uses a 2D array to store the intermediate results, allowing efficient access and reuse.
        """
        n = len(Values)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if j >= Weights[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], Values[i - 1] + dp[i - 1][j - Weights[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][W]
