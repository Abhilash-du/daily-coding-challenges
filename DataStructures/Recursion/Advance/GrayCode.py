# Problem Description
# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.
#
# Problem Constraints
# 1 <= A <= 16
#
# Input Format
# The first argument is an integer A.
#
# Output Format
# Return an array of integers representing the gray code sequence.
#
# Example Input
# Input 1: A = 2
# Input 1: A = 1
#
# Example Output
# output 1: [0, 1, 3, 2]
# output 2: [0, 1]
#
# Example Explanation
# Explanation 1:
# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].
#
# Explanation 1:
# for A = 1 the gray code sequence is:
#     00 - 0
#     01 - 1
# So, return [0, 1].
class Solution:
    def convertToDecimal(self, val):
        val = int(val)
        i = 0
        ans = 0
        while val > 0:
            ans += (2 ** i) * (val % 10)
            i += 1
            val = val // 10
        return ans

    def convertToGrayCode(self, A):
        if A == 1:
            return [0, 1]

        preA = self.convertToGrayCode(A - 1)
        n = len(preA)
        ans = []
        for val in preA:
            ans.append(str(0) + str(val))

        for i in range(n):
            val = preA[n - i - 1]
            ans.append(str(1) + str(val))
        return ans

    def grayCode(self, A):  # mainMethod
        ans = self.convertToGrayCode(A)
        n = len(ans)
        for i in range(n):
            ans[i] = self.convertToDecimal(ans[i])
        return ans

# Solution Approach:-
# 1. The function get_gray_codes is defined.
# 2. It takes the number of bits n as argument.
# 3. It returns n-bit Gray code in a list.
# 4. The function works by first obtaining the (n – 1)-bit Gray code.
# 5. The first half of the n-bit Gray codewords are simply the (n – 1)-bit Gray codewords prepended by a 0.
# 6. The second half of the n-bit Gray codewords are (n – 1)-bit Gray codewords listed in reverse and
# prepended with a 1.
# 7. The 0-bit Gray code simply consists of the empty string.
