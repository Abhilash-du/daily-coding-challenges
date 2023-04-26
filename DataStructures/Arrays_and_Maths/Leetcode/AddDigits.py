"""
258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:

    # Approach 1:-
    def addDigits_approach_1(self, num: int) -> int:
        # Initialize variables
        val = num  # 'val' holds the current value being evaluated
        sum = 0  # 'sum' will hold the sum of the digits of 'val'

        # Loop until 'val' becomes a single-digit number
        while (val > 9):
            # Reset 'sum' for the next iteration
            sum = 0
            # Extract the digits of 'val' one by one and add them to 'sum'
            while (val != 0):
                sum += val % 10  # Add the last digit of 'val' to 'sum'
                val = val // 10  # Remove the last digit from 'val'
            # Update 'val' to be the new sum of its digits
            val = sum

        # Once 'val' is a single-digit number, return it (this is the digital root)
        return val

    # optimized way (Approach-2):-
    def addDigits(self, num: int) -> int:
        # If the input number is 0, return 0 as the digital root
        if (num == 0):
            return 0

        # If the input number is divisible by 9, return 9 as the digital root
        if (num % 9 == 0):
            return 9

        # Otherwise, return the remainder when the input number is divided by 9
        return num % 9


"""
Approach 1:-
The code is implementing a method addDigits which takes an integer num as input and returns the digital root of num. 
The digital root of a number is obtained by repeatedly summing its digits until a single-digit value is obtained.

The implementation starts by initializing two variables val and sum to num and 0, respectively. Then, the code enters 
a loop that continues until val becomes a single-digit number.

Inside the loop, the code resets sum to 0 and extracts the digits of val one by one using the modulus and integer 
division operations. It adds each digit to sum and removes it from val until there are no more digits left in val.

After computing the sum of the digits of val, the code updates val to be the new sum of its digits. This process 
continues until val becomes a single-digit number.

Finally, the digital root of num is the single-digit number that val has become. Therefore, the code returns val.

The time complexity of the implementation is O(log n), where n is the value of num. This is because the loop 
continues until val becomes a single-digit number, which requires O(log n) iterations in the worst case. Within each 
iteration, the code extracts the digits of val one by one, which takes O(log n) time in the worst case. Therefore, 
the overall time complexity of the implementation is O(log n) + O(log n) = O(log n).

##########################


Approach 2:- 

The goal of the program is to find the digital root of a given positive integer 'num'. The digital root 
of a number is the single-digit value obtained by repeatedly summing the digits of the number until a single-digit 
value is obtained.

For example, the digital root of 123 is 6 because 1+2+3 = 6, and 6 is a single digit. Similarly, the digital root of 
456 is 6 because 4+5+6 = 15, and 1+5 = 6.

Now, let's take a look at the code. The code has three main parts:

The first if statement checks if the input number is 0. If it is, then the digital root is 0, and the function returns 0.

The second if statement checks if the input number is divisible by 9. If it is, then the digital root is 9, 
and the function returns 9. This is because any number that is divisible by 9 will have a digital root of 9.

If the input number is not 0 and not divisible by 9, then the program computes the sum of the digits of the input 
number, and returns the remainder of this sum when divided by 9. This is because the digital root of a number is 
equivalent to the remainder of the sum of its digits when divided by 9.

To understand why the third part of the code works, consider the following example:

Suppose the input number is 567. The sum of its digits is 5+6+7 = 18. The digital root of 567 is the single-digit 
value obtained by repeatedly summing the digits of 567 until a single-digit value is obtained. Since 18 is not a 
single digit, we need to repeat the process by summing the digits of 18. The sum of the digits of 18 is 1+8 = 9. 
Therefore, the digital root of 567 is 9.

Now, let's see how the third part of the code computes the digital root of 567. Since 5+6+7 = 18, the code computes 
the remainder of 18 when divided by 9, which is 0. However, since 567 is not divisible by 9, the digital root of 567 
cannot be 0. Therefore, we need to repeat the process by summing the digits of 18, which gives us 1+8 = 9. Therefore, 
the digital root of 567 is 9, which is correctly returned by the code.

In general, the third part of the code works because the remainder of the sum of the digits of a number when divided 
by 9 is equivalent to the digital root of the number, unless the sum is divisible by 9. In the latter case, 
the digital root is 9."""
