"""
Problem Description
Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.
Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
Since the answer can be large, output answer modulo 1000000007

Problem Constraints
1 <= A <= 1000
1 <= B <= 10000

Input Format
First argument is the integer A
Second argument is the integer B

Output Format
Return a single integer, the answer to the problem

Example Input
Input 1:
 A = 2
 B = 4

Input 2:
 A = 1
 B = 3

Example Output
Output 1: 4
Output 2: 1

Example Explanation
Explanation 1:
 Valid numbers are {22, 31, 13, 40}
 Hence output 4.

Explanation 2:
 Only valid number is 3
"""

import sys

sys.setrecursionlimit(100000)


class Solution:
    # Constructor to initialize the class
    def __init__(self):
        self.MOD = 1000000007  # Modulo value for calculations

    def solve(self, A, B):
        dp = [[-1 for i in range(B + 1)] for _ in range(A + 1)]  # 2D array for memoization
        ans = 0  # Initialize the answer to 0

        # Iterate over the possible first digits from 1 to 9
        for i in range(1, 10):
            ans += self.countRecord(A - 1, B - i, dp)  # Accumulate the count by calling countRecord
            ans %= self.MOD  # Apply modulo operation to avoid overflow

        return ans  # Return the final answer modulo MOD

    def countRecord(self, digits, expected_sum, dp):
        # Base cases
        if expected_sum < 0: return 0  # If the expected sum is negative, return 0 (invalid combination)
        if digits == 0 and expected_sum == 0: return 1 # If no digits are left and the sum is 0,its a valid combination)
        if digits <= 0: return 0  # If no digits are left and the sum is not 0, return 0 (invalid combination)

        if dp[digits][expected_sum] != -1:
            return dp[digits][expected_sum]  # If the result is already computed, return it from the dp array

        ans = 0  # Initialize the answer to 0

        # Iterate over the possible digits from 0 to 9
        for i in range(10):
            ans += self.countRecord(digits - 1, expected_sum - i,
                                    dp)  # Accumulate the count by calling countRecord recursively
            ans %= self.MOD  # Apply modulo operation to avoid overflow

        dp[digits][expected_sum] = ans  # Store the result in the dp array for future reference
        return ans  # Return the final answer


"""
The code aims to find the count of A-digit positive numbers whose digits, when added together, equal a given number B.
It uses dynamic programming and recursion with memoization to optimize the computation.

The solution is divided into two functions: solve() and countRecord().

Approach:
- The solve() function initializes a 2D array dp for memoization and sets the answer to 0.
- It iterates over the possible first digits from 1 to 9.
- Inside the loop, it accumulates the count by calling the countRecord() function for each possible first digit and 
    applies modulo operation to avoid overflow.
- The countRecord() function handles the recursive calculation of the count based on the remaining digits and expected
    sum.
- It includes base cases to handle invalid and valid combinations.
- It checks if the result for the given parameters is already computed in the dp array and returns it if available.
- Otherwise, it recursively calls itself for each possible digit and accumulates the count.
- The result is stored in the dp array for future reference and returned as the final answer.

Time Complexity:
- The time complexity of the solution is determined by the number of unique subproblems.
- Since there are A * B unique subproblems, the time complexity is O(A * B).

Space Complexity:
- The space complexity is determined by the size of the memoization array.
- The memoization array has dimensions (A+1) x (B+1), resulting in a space complexity of O(A * B).
"""
