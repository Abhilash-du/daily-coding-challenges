# Problem Description
# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
#
# # Problem Constraints
# 1 <= |A| <= 1000
#
# Input Format
# The first and only argument contains the string A, consisting of lowercase English alphabets.
#
# Output Format
# Return an integer containing the answer.
#
# Example Input
# Input 1:  "abobc"
# Input 2:  "bobob"
#
# Example Output
# Output 1:  1
# Output 2:  2
#
# Example Explanation
# Explanation 1:   The only occurrence is at second position.
# Explanation 2:   Bob occurs at first and third position.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        i = 1
        while i < n - 1:
            if A[i - 1] == "b" and A[i + 1] == "b" and A[i] == "o":
                count += 1
                i += 2  # if bob is formed, then i+1 element cannot create bob string
            else:
                i += 1
        return count

# Observation / Approach:-
# Iterate over the string and for each index i starting from 1 to n-2 check whether substring
# formed by the index i-1, i and i+1 is "bob" if yes then increase index by 2
# else: increase index by 1
# answer. You can also use inbuilt function for the same if it is present
# in your preferred language.
