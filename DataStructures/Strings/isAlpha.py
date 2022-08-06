# Problem Description
# You are given a function isalpha() consisting of a character array A.
# Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.
#
# Problem Constraints: 1 <= |A| <= 105
#
# Input Format: Only argument is a character array A.
#
# Output Format: Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.
#
# Example Input
# Input 1:  A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
# Input 2:  A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
#
# Example Output
# Output 1:  1
# Output 2:  0
#
# Example Explanation
# Explanation 1:  All the characters are alphabets.
# Explanation 2:  All the characters are NOT alphabets i.e ('#', '2', '0', '2', '0').

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        flag = 0
        for char_val in A:
            ascii_val = ord(char_val)
            if 64 < ascii_val < 91 or 96 < ascii_val < 123:
                flag = 1
            else:
                flag = 0
                break
        return flag

# To execute:-
# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
# alphaCheck = Solution()
# print(alphaCheck.solve(A))
