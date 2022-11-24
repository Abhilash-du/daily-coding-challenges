# Problem Description
# Given an integer A, you have to find the Ath Perfect Number.
# A Perfect Number has the following properties:
# It comprises only 1 and 2.
# The number of digits in a Perfect number is even. It is a palindrome number.
#
# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.
#
# Problem Constraints
# 1 <= A <= 100000
#
# Input Format
# The only argument given is an integer A.
#
# Output Format
# Return a string that denotes the Ath Perfect Number.
#
# Example Input
# Input 1:  A = 2
# Input 2:  A = 3
#
# Example Output
# Output 1:  22
# Output 2:#  1111
#
# Example Explanation
# Explanation 1:
# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221
# Explanation 2:
# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        k = 0
        queue = ["11", "22"]
        ans = queue[0]
        k = 0
        while k != A:
            ans = queue.pop(0)
            n = len(ans)
            mid = n // 2
            queue.append(ans[0:mid] + "11" + ans[mid:n])
            queue.append(ans[0:mid] + "22" + ans[mid:n])
            k += 1
        return ans

# Observation/Solution Approach:-
#                  11 22
#           1111 1221 2112 2222
#  111111 112211 121121 122221 211112 212212
#
# As we can check the number are repeating in the middle of each element: 11, 22
# So basically we can use queue amd in loop we can keep appending value and removing the top value as answer
