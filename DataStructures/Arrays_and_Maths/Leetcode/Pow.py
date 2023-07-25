"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to efficiently compute the power without exceeding the given constraints.

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Define the recursive helper function to calculate power
        def power(num, pwr):
            if pwr == 0:  # Base case: any number raised to the power of 0 is 1
                return 1

            if pwr < 0:  # If power is negative, calculate the reciprocal
                return power(1.0 / num, -1 * pwr)

            if (pwr & 1) == 1:  # If power is odd
                # Divide power by 2 (integer division) and recursively multiply
                return num * power(num * num, (pwr - 1) // 2)

            else:  # If power is even
                return power(num * num, pwr // 2)  # Divide power by 2 (integer division) and recursively multiply

        return power(x, n)  # Call the helper function to calculate the result


"""
Intuition:
The myPow function aims to calculate the result of x raised to the power n using a recursive approach. 
We divide and conquer the problem by reducing the power in each step, making it an efficient algorithm. 
The function handles both positive and negative powers.

Time Complexity (TC):
The time complexity of the myPow function is O(log n) because we halve the power in each recursive call. 
As a result, the number of recursive calls is proportional to the logarithm of the power, making it an efficient 
calculation even for large values of n.

Space Complexity (SC):
The space complexity of the myPow function is O(log n) as well. This is because the recursion creates a call stack, 
and the space used is proportional to the height of the recursion tree. Since we divide the power in half with each 
recursive call, the maximum height of the recursion tree is log n. Therefore, the space used is logarithmic, 
making the function memory-efficient.
"""
