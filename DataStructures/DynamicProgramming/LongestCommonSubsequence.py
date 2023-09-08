"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the length of such longest common subsequence.

Q6. Longest Common Subsequence
Problem Description
Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous),
which is common in both the strings.
You need to return the length of such longest common subsequence.

Problem Constraints
1 <= Length of A, B <= 1005

Input Format
First argument is a string A.
Second argument is a string B.

Output Format
Return an integer denoting the length of the longest common subsequence.

Example Input
Input 1:
 A = "abbcdgf"
 B = "bbadcgf"

Input 2:
 A = "aaaaaa"
 B = "ababab"

Example Output
Output 1: 5
Output 2: 3

Example Explanation
Explanation 1: The longest common subsequence is "bbcgf", which has a length of 5.
Explanation 2: The longest common subsequence is "aaa", which has a length of 3.
"""


class Solution:
    def longestCommonSubsequence(self, A, B):
        # Get the lengths of strings A and B
        len_A, len_B = len(A), len(B)

        # Create a 2D DP table to store the length of LCS
        dp = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]

        # Populate the DP table
        for i in range(1, len_A + 1):
            for j in range(1, len_B + 1):
                if A[i - 1] == B[j - 1]:
                    # If the current characters match, increment the LCS length
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If they don't match, take the maximum of the LCS without the current character
                    # in either A or B
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The value at dp[len_A][len_B] will be the length of the LCS
        return dp[len_A][len_B]


"""
███ Intuition ███

The code aims to find the Longest Common Subsequence (LCS) between two strings, A and B. It utilizes dynamic 
programming to efficiently compute the length of the LCS.

1. Create a 2D DP table, dp, where dp[i][j] represents the length of the LCS between the first i characters of string
 A and the first j characters of string B.

2. Initialize the DP table with zeros.

3. Iterate through each character in strings A and B using nested loops:

    a. If the current characters A[i-1] and B[j-1] match, it indicates they are part of the LCS. Increment the LCS 
        length by 1 and consider the previous characters' LCS length (dp[i-1][j-1]).

    b. If the current characters do not match, choose the maximum LCS length from either excluding the current character
        in A (dp[i-1][j]) or excluding the current character in B (dp[i][j-1]).

4. Continue filling the DP table for all possible combinations of characters in A and B.

5. The value at dp[len_A][len_B] represents the length of the LCS of the entire strings A and B.

6. Return this LCS length as the result.

This dynamic programming approach efficiently computes the length of the LCS by considering overlapping subproblems and 
provides the desired result.


Time Complexity (TC):

The time complexity of this code is O(n*m), where n is the length of string A and m is the length of string B. 
This is because we use a nested loop that iterates over all characters of both strings to fill the DP table. Each cell 
of the DP table requires constant time operations.

Space Complexity (SC):

The space complexity of this code is O(n*m) as well. We create a 2D DP table of size (n+1) x (m+1) to store the 
intermediate LCS lengths. Therefore, the space required is directly proportional to the product of the lengths of 
strings A and B.
"""
