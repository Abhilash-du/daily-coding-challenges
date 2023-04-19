"""
Q4. Add Binary Strings

Problem Description
Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.

Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"

Example Output
Output 1:
"111"
Output 2:
"1000"

Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:

The sum of 110 and 10 is 1000.

"""
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        ptr_a = len(A) - 1
        ptr_b = len(B) - 1
        carry = 0
        ans = ""

        while ptr_a >= 0 or ptr_b >= 0:
            val1 = A[ptr_a] if ptr_a >= 0 else "0"
            val2 = B[ptr_b] if ptr_b >= 0 else "0"

            sum_val = int(val1) + int(val2) + carry
            ans = str(sum_val % 2) + ans
            carry = sum_val // 2
            ptr_a -= 1
            ptr_b -= 1

        ans = "1" + ans if carry > 0 else ans
        return ans


"""
We traverse both the binary strings A and B from right to left, adding their corresponding bits and the carry 
obtained from the previous addition. The sum of the two bits is obtained using the int function, and the carry is 
computed as the integer division of the sum by 2. The remainder of the sum divided by 2 is the value of the current 
bit in the resulting binary sum.

If the length of the two input strings A and B is not the same, we consider the shorter string as having leading 0's. 
Once the traversal is completed, we check if there is any carry remaining, which needs to be added to the most 
significant bit in the sum. Finally, we return the resulting binary string.

The time complexity of the given algorithm is O(N), where N is the maximum length of the two input strings A and B. 
This is because we traverse each string only once.

The space complexity of the algorithm is O(N), where N is the length of the resulting binary string. This is because 
we are storing the result in a string variable named ans.
"""
