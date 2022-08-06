# Problem Description
# You are given a function to_upper() consisting of a character array A.
# Convert each charater of A into Uppercase character if it exists.
# If the Uppercase of a character does not exist, it remains unmodified.
# The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
# Return the uppercase version of the given character array.
#
# Problem Constraints: 1 <= |A| <= 105
#
# Input Format: Only argument is a character array A.
#
# Output Format: Return the uppercase version of the given character array.
#
# Example Input
# Input 1:  A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
# Input 2:  A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
#
# Example Output
# Output 1:  ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']
# Output 2:  ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']
#
# Example Explanation
# Explanation 1: All the characters in the returned array are in uppercase alphabets.

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        n = len(A)
        for i in range(n):
            ascii_val = ord(A[i])
            if 96 < ascii_val < 123:
                A[i] = chr(ascii_val ^ (1 << 5))  # logic to toggle character
        return A


# to execute:-
A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y', 'z']
toggle_lower = Solution()
print(toggle_lower.to_upper(A))
