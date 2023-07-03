"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the minimum health of the last surviving person.

Q4. Pubg
Problem Description
There are N players, each with strength A[i]. when player i attack player j,
player j strength reduces to max(0, A[j]-A[i]).
When a player's strength reaches zero, it loses the game, and the game continues in the same manner among other players
until only 1 survivor remains.

Can you tell the minimum health last surviving person can have?

Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 1000000

Input Format
First and only argument of input contains a single integer array A.

Output Format
Return a single integer denoting minimum health of last person.

Example Input
Input 1: A = [6, 4]
Input 2: A = [2, 3, 4]

Example Output:-
Output 1: 2
Output 2: 1

Example Explanation
Explanation 1:
 Given strength array A = [6, 4]
 Second player attack first player, A =  [2, 4]
 First player attack second player twice. [2, 0]

Explanation 2:
 Given strength array A = [2, 3, 4]
 First player attack third player twice. [2, 3, 0]
 First player attack second player. [2, 1, 0]
 Second player attack first player twice. [0, 1, 0]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Function to calculate the greatest common divisor (GCD) using Euclid's algorithm
        def euclidsGCD(a, b):
            if b == 0:
                return max(a, b)
            return euclidsGCD(b, a % b)

        prev = A[0]  # Initialize the previous strength as the first player's strength
        for i in range(len(A)):
            val = euclidsGCD(prev, A[i])  # Calculate the GCD of the previous strength and the current player's strength
            if val == 1:  # If the GCD is 1, the minimum health of the last person will be 1
                return 1
            prev = val  # Update the previous strength to the calculated GCD

        return val  # Return the minimum health of the last person

"""
Intuition:

The problem involves simulating a game scenario where players attack each other, and the goal is to determine the
minimum health of the last surviving person. The code uses the concept of the greatest common divisor (GCD) to 
calculate the remaining strength of a player after an attack.

The code iterates through the array of player strengths, starting from the second player.
For each player, it calculates the GCD between the previous player's strength and the current player's strength. 
If the GCD is 1 at any point, it means that the minimum health of the last person will be 1, as a GCD of 1 indicates 
that the remaining strength cannot be further reduced.

The code updates the previous player's strength to the calculated GCD and continues the iteration. 
After the loop, the code returns the value of the last calculated GCD,
which represents the minimum health of the last person.

The solution utilizes the Euclidean algorithm for calculating the GCD efficiently.
By iteratively finding the remainder of the division, the algorithm converges to the GCD.
This approach reduces the strength of players effectively until only one survivor remains.

Overall, the intuition behind the solution is to iteratively calculate the GCD of player strengths and determine the 
minimum health of the last person based on the GCD value.

Time Complexity:
The time complexity of the code is O(N), where N is the number of players or the length of the input array A. 
This is because the code iterates through the array once, performing constant-time operations for each element. 
Therefore, the time complexity is linear with respect to the size of the input.

Space Complexity:
The space complexity of the code is O(1) or constant. 
This is because the code uses a constant amount of space for variables prev, i, val, and the helper function 
euclidsGCD(). The space used does not depend on the input size or the number of players. 

Hence, the space complexity is constant.
"""