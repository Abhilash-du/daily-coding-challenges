# Problem Description
#
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a
# different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string
# B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else,
# return 0.
#
# Problem Constraints
# 1 <= N, length of each word <= 105
# Sum of the length of all words <= 2 * 106
#
# Input Format:
# The first argument is a string array A of size N.
# The second argument is a string B of size 26, denoting the order.
#
# Output Format
# Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
#
# Example Input
# Input 1:
#  A = ["hello", "scaler", "interviewbit"]
#  B = "adhbcfegskjlponmirqtxwuvzy"
#
# Input 2:
#  A = ["fine", "none", "no"]
#  B = "qwertyuiopasdfghjklzxcvbnm"
#
# Example Output
# Output 1:  1
# Output 2:  0
#
# Example Explanation
# Explanation 1:  The order shown in string B is: h < s < i for the given words. So return 1.
# Explanation 2:  "none" should be present after "no". Return 0.
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        order_map = {c: i for i, c in enumerate(B)}  # hashmap to store order key-value pairs
        n = len(A)
        for i in range(n - 1):  # comparing 2 elements at a time
            w1, w2 = A[i], A[i + 1]
            for k in range(len(w1)):
                if k >= len(w2):  # if w1 and w2 has same character but length of w1 is greater
                    return 0
                char1, char2 = w1[k], w2[k]
                if char1 != char2:  # comparing each character
                    if order_map[char1] > order_map[char2]:
                        return 0
                    break  # break because two characters are in perfect order(we don't need to check further)
        return 1

# Solution Approach/Observation:-
# Let’s check whether all adjacent words a and b have a <= b.
#
# To check whether a <= b for two adjacent words, a and b, we can find their first difference.
# For example, “applying” and “apples” have the first difference of y and e.
# After, we compare these characters to the index in order.
#
# Care must be taken to deal with the blank character effectively.
# If, for example, we are comparing “app” to “apply”, the first difference is between (null) and “l”.
