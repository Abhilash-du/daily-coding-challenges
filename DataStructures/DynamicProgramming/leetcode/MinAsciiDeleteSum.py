"""
712. Minimum ASCII Delete Sum for Two Strings
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.

"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)

        # Create a 2D array to store the dynamic programming values
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

        # Initialize the first row and first column of the dp array
        dp[0][0] = 0

        for c in range(1, n1 + 1):
            # Calculate the accumulated ASCII sum for string s1
            dp[0][c] = dp[0][c - 1] + ord(s1[c - 1])

        for r in range(1, n2 + 1):
            # Calculate the accumulated ASCII sum for string s2
            dp[r][0] = dp[r - 1][0] + ord(s2[r - 1])

        # Iterate through the dp array to find the minimum ASCII sum of deleted characters
        for rw in range(1, n2 + 1):
            for cl in range(1, n1 + 1):
                if s1[cl - 1] == s2[rw - 1]:
                    # If the characters are the same, no deletion is needed
                    dp[rw][cl] = dp[rw - 1][cl - 1]
                else:
                    # If the characters are different, choose the minimum sum of deletions
                    # considering deleting the current character from either s1 or s2
                    val1 = ord(s1[cl - 1]) + dp[rw][cl - 1]
                    val2 = ord(s2[rw - 1]) + dp[rw - 1][cl]
                    dp[rw][cl] = min(val1, val2)

        # The value at dp[n2][n1] represents the minimum ASCII sum of deleted characters
        # needed to make s1 and s2 equal
        return dp[n2][n1]

"""
Intuition:
The problem can be solved using dynamic programming. The idea is to find the minimum ASCII sum of deleted characters 
required to make two strings equal. To do this, we use a 2D array dp, where dp[i][j] represents the minimum ASCII sum 
of deleted characters needed to make the prefixes of s1 of length i and s2 of length j equal.

The dynamic programming approach is based on the observation that if the characters at the current positions s1[i-1] 
and s2[j-1] are the same, then we don't need to delete any character at these positions. So, dp[i][j] will be the same 
as dp[i-1][j-1].

However, if the characters at the current positions are different, we have two options:

1. Delete the character at s1[i-1], which would add its ASCII value to the sum, and we consider the state dp[i][j-1].

2. Delete the character at s2[j-1], which would add its ASCII value to the sum, and we consider the state dp[i-1][j].
We take the minimum of these two options and store it in dp[i][j].

Time Complexity (TC):
The time complexity of this solution is O(n1 * n2), where n1 and n2 are the lengths of s1 and s2, respectively. 
This is because we use a nested loop to fill the dp array, and each cell is filled in constant time.

Space Complexity (SC):
The space complexity of this solution is O(n1 * n2) as well. 
This is because we use a 2D array dp of size (n2+1) x (n1+1) to store the dynamic programming values. 
This space is required to store the intermediate results for each combination of prefixes of s1 and s2.
"""