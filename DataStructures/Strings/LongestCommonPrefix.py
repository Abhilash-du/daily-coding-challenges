# Problem Description
# Given the array of strings A, you need to find the longest string S, which is the prefix of ALL
# the strings in the array.
#
# The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
# and S2.
#
# Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
# Problem Constraints
# 0 <= sum of length of all strings <= 1000000
#
# Input Format
# The only argument given is an array of strings A.
#
# Output Format
# Return the longest common prefix of all strings in A.
#
# Example Input
# Input 1: A = ["abcdefgh", "aefghijk", "abcefgh"]
# Input 2: A = ["abab", "ab", "abcd"];
#
# Example Output
# Output 1: "a"
# Output 2: "ab"
#
# Example Explanation
# Explanation 1: Longest common prefix of all the strings is "a".
# Explanation 2: Longest common prefix of all the strings is "ab".
#
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        min_len = 10 ** 9
        max_val = -10 ** 9

        # finding the minimum length and maximum length string
        ans = ""
        for val in A:
            k = len(val)
            min_len = min(min_len, k)
            if max_val < k:
                ans = val  # finding the max length string

        # finding the common element
        count = 0
        for i in range(min_len):
            first_char = A[0][i]
            flag = False
            for val in A:
                if first_char == val[i]:
                    flag = True
                else:
                    flag = False
                    break
            if not flag:
                break
            else:
                count += 1  # number of common element
        return ans[:count]

# Approach Followed:-
# Note: the prefix has to be the prefix of ALL the strings.
#
# So, you can pick any random string from the array and
# start checking its characters from the beginning to see if they can be a part of the common substring.
