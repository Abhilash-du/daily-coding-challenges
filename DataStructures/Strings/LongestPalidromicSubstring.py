# Problem Description
# Given a string A of size N, find and return the longest palindromic substring in A.
# Substring of string A is A[i...j] where 0 <= i <= j < len(A)
#
# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
# In case of conflict, return the substring which occurs first ( with the least starting index).
#
# Problem Constraints
# 1 <= N <= 6000
#
# Input Format
# First and only argument is a string A.
#
# Output Format
# Return a string denoting the longest palindromic substring of string A.
#
# Example Input
# Input 1: A = "aaaabaaa"
# Input 2: A = "abba
#
# Example Output
# Output 1: "aaabaaa"
# Output 2: "abba"
#
# Example Explanation
#  1: We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
# Explanation 2: We can see that longest palindromic substring is of length 4 and the string is "abba".
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, str):
        n = len(str)
        # for odd length
        start, end = 0, 0
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and str[left] == str[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start = left + 1
                end = right

            # for right length
            left = i
            right = i + 1
            while left >= 0 and right < n and str[left] == str[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start = left + 1
                end = right
        return str[start:end]

# Approach Followed:-
# In this approach, we iterate over all the possible centers of a palindrome in the given string.
# There are two types of centers - one is a single character and the other is a pair of adjacent characters.
# For each center, we expand in both directions as long as the characters on both sides are equal.
#
# We keep track of the longest palindrome seen so far and update it whenever we find a longer palindrome.
# At the end, we return the longest palindrome.
# The time complexity of this approach is O(N^2) and the space complexity is O(1).
