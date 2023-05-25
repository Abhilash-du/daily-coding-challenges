"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the count of lucky numbers

Problem Description
A lucky number is a number that has exactly 2 distinct prime divisors.
You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive)

Problem Constraints
1 <= A <= 50000

Input Format
The first and only argument is an integer A.

Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.

Example Input
Input 1: A = 8
Input 2: A = 12

Example Output
Output 1: 1
Output 2: 3

Example Explanation
Explanation 1: Between [1, 8] there is only 1 lucky number i.e 6. 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2: Between [1, 12] there are 3 lucky number: 6, 10 and 12.

"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        p_list = [0] * (A + 1)

        # Sieve of Eratosthenes to find prime numbers
        for i in range(2, A):
            if p_list[i] != 0:
                continue
            num = 2
            while i * num <= A:
                p_list[i * num] += 1
                num += 1

        lucky_count = 0
        # Count numbers with exactly 2 distinct prime divisors
        for val in p_list:
            if val == 2:
                lucky_count += 1
        return lucky_count


"""
Approach:
1. Initialize a list to store the count of factors for each number from 0 to A.
2. Use the Sieve of Eratosthenes algorithm to find prime numbers up to A.
3. For each prime number, update the count of factors for its multiples.
4. Count the numbers that have exactly 2 distinct prime divisors.
5. Return the count of lucky numbers.

Time Complexity:
The time complexity of this solution is O(A), where A is the input number.
The Sieve of Eratosthenes algorithm takes O(A) time to find prime numbers,
and counting the lucky numbers also takes O(A) time.
Thus, the overall time complexity is O(A).

Space Complexity:
The space complexity (SC) of the given code is determined by the additional space used by the p_list list,
which stores the count of factors for each number from 0 to A. The size of p_list is (A + 1), as it includes 
the count of factors for numbers from 0 to A.
Therefore, the space complexity of the code is O(A), as it requires additional space proportional to the input number A.
"""
