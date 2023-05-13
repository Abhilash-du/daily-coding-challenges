"""
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.
A good string is a string constructed by the above process having a length between low and high (inclusive).
Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation:
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".


Constraints:
1 <= low <= high <= 10^5
1 <= zero, one <= low
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Define a constant variable to be used later
        MOD = (10 ** 9) + 7

        # Initialize an array with -1's with a size of high+1
        dp = [-1 for _ in range(high + 1)]

        # Define a recursive function to solve the problem
        def solve(str_len, dp):
            # If the current string length exceeds the given high limit, return 0
            if (str_len > high):
                return 0

            # If the current string length has already been calculated, return the value
            if (dp[str_len] != -1):
                return dp[str_len]

            # Set current element to 1 if the current length is within the given low and high limits
            current_element = 0
            if (str_len <= high and str_len >= low):
                current_element = 1

            # Recursive call to calculate the number of strings with 'zero' and 'one' appended to it
            append_zero = solve(str_len + zero, dp)
            append_one = solve(str_len + one, dp)

            # Store the calculated value in the dp array
            dp[str_len] = (current_element + append_zero + append_one) % MOD

            # Return the calculated value
            return dp[str_len]

        # Call the recursive function with initial string length of 0 and return the result
        return solve(0, dp)

"""
Intuition
The dp array is used to store the previously calculated values to avoid recomputation of the same subproblems. 
By using the solve() function recursively, we are dividing the problem into subproblems and solving them one by one. 
We are using dynamic programming to avoid recomputation of previously solved subproblems.

Time and Space Complexity
The time complexity of this solution is O(high), where high is the maximum length of the good string. 
This is because we are solving the problem for each string length from 0 to high exactly once.

The space complexity of this solution is also O(high), as we are using an array of size high+1 to store the previously 
calculated values.

"""
