# Problem Description
# You are given a string A of size N.
# Return the string A after reversing the string word by word.
#
# NOTE:
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
#
# Problem Constraints
# 1 <= N <= 3 * 105
#
# Input Format: The only argument given is string A.
#
# Output Format: Return the string A after reversing the string word by word.
#
# Example Input:-
# Input 1:
#     A = "the sky is blue"
# Input 2:
#     A = "this is ib"
#
# Example Output
# Output 1: "blue is sky the"
# Output 2: "ib is this"
#
# Example Explanation
# Explanation 1: We reverse the string word by word so the string becomes "the sky is blue".
# Explanation 2: We reverse the string word by word so the string becomes "this is ib".
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.split()
        n = len(A)
        for i in range(n // 2):
            A[i], A[n - i - 1] = A[n - i - 1], A[i]
        return " ".join(A)


# For Execution
A = "the sky is blue"
B = "this is ib"
reverseString = Solution()
print(reverseString.solve(A))
print(reverseString.solve(B))

# Approach followed and Observations:-
# One simple approach is a two-pass solution:
#
# First pass to split the string by spaces into an array of words
# Then second pass to extract the words in reversed order
