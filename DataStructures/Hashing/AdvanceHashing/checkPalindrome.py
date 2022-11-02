# Q3. Check Palindrome - II
#
# Problem Description
# Given a string A consisting of lowercase characters.
#
# Check if characters of the given string can be rearranged to form a palindrome.
#
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else
# return 0.
#
#
#
# Problem Constraints
# 1 <= |A| <= 105
#
# A consists only of lower-case characters.
#
#
#
# Input Format
# First argument is an string A.
#
#
#
# Output Format Return 1 if it is possible to rearrange the characters of the string A such that it becomes a
# palindrome else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = "abcde"
# Input 2:
#
#  A = "abbaee"
#
#
# Example Output
# Output 1:
#
#  0
# Output 2:
#
#  1
#
#
# Example Explanation
# Explanation 1:
#
#  No possible rearrangement to make the string palindrome.
# Explanation 2:
#
#  Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 1:
            return 1
        flag = False
        if n // 2 != 0:
            flag = True
        hmap = {}

        for val in A:
            if val in hmap:
                hmap[val] += 1
            else:
                hmap[val] = 1

        for val in hmap:
            if hmap[val] % 2 != 0 and flag == True:
                flag = False
            elif hmap[val] % 2 != 0:
                return 0
        return 1

# Approach/Followed:-
# the count of palindromic characters should be even (in case of even number of characters)
# if the number of characters is odd: there can be one character which is odd

