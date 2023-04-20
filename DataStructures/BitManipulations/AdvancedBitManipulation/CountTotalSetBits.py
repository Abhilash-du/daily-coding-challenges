"""Problem Description Given a positive integer A, the task is to count the total number of set bits in the binary
representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.

Problem Constraints
1 <= A <= 10^9

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )
modulo 10^9 + 7.

Example Input
Input 1: A = 3
Input 2: A = 1

Example Output
Output 1: 4
Output 2: 1

Example Explanation
Explanation 1:

 DECIMAL    BINARY  SET BIT COUNT
    1          01        1
    2          10        1
    3          11        2
 1 + 1 + 2 = 4
 Answer = 4 % 1000000007 = 4
Explanation 2:

 A = 1
  DECIMAL    BINARY  SET BIT COUNT
    1          01        1
 Answer = 1 % 1000000007 = 1

"""


class Solution:
    # Function to find the number of ones in the binary representation
    # of all the numbers from 0 to N (inclusive).
    # @param N: An integer representing the upper limit of the range.
    # @return: An integer representing the number of ones in the binary
    # representation of all the numbers from 0 to N (inclusive).
    def solve(self, N):
        # Set the modulo value as 10^9+7.
        MOD = 10 ** 9 + 7

        # Increment N by 1 as we need to include N in the range.
        N += 1

        # Initialize the set size to 2 and the answer to 0.
        set_size = 2
        ans = 0

        # Iterate until the set size is greater than or equal to the
        # number of elements in the set.
        while N >= (set_size // 2):

            # Calculate the total number of sets that can be formed
            # using the current set size.
            total_sets = N // set_size

            # Calculate the total number of ones in each set.
            total_ones = total_sets * (set_size // 2)

            # Add the total number of ones to the answer.
            ans += total_ones

            # Check if there are any remaining elements in the set and
            # if so, calculate the number of ones in the remaining elements.
            if N % set_size > (set_size // 2):
                ans += (N % set_size) - (set_size // 2)

            # Take the modulo of the answer with the given modulo value.
            ans %= MOD

            # Double the set size.
            set_size *= 2

        # Return the final answer.
        return ans


"""
Approach Followed:-
The time complexity of the given code is O(log(N)), where N is the upper limit of the range. 
The space complexity is O(1), as the code only uses a fixed number of variables.

The logic behind the code is to count the number of ones in the binary representation of all the numbers from 0 to N 
(inclusive) using bit manipulation techniques. The code works by iterating through all possible set sizes
 and counting the number of ones in each set.

For each set size, the code calculates the total number of sets that can be formed using that set size. 
It then calculates the total number of ones in each set by multiplying the number of sets by half of the set size,
 since each set contains an equal number of zeros and ones.

The code then adds the total number of ones in each set to the answer. If there are any remaining elements in the set,
 the code calculates the number of ones in those elements and adds it to the answer.

The set size is then doubled, and the process is repeated until the set size is greater than or equal to the number of 
elements in the set. Finally, the code returns the final answer,
 taking the modulo of the answer with the given modulo value.

I hope this explanation helps! Let me know if you have any further questions.
"""
