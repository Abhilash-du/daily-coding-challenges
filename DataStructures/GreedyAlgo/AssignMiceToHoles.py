"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to assign Mice to Holes

Problem Description
N Mice and N holes are placed in a straight line. Each hole can accommodate only one mouse.
The positions of Mice are denoted by array A, and the position of holes is denoted by array B.

A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1.
 Any of these moves consume 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

Problem Constraints
1 <= N <= 10^5
-109 <= A[i], B[i] <= 10^9

Input Format
The first argument is an integer array A.
The second argument is an integer array B.

Output Format
Return an integer denoting the minimum time when the last nouse gets inside the holes.

Example Input
Input 1:
 A = [-4, 2, 3]
 B = [0, -2, 4]

Input 2:
 A = [-2]
 B = [-6]

Example Output
Output 1: 2
Output 2: 4


Example Explanation:-
Explanation 1:
 Assign the mouse at position (-4 to -2), (2 to 0) and (3 to 4).
 The number of moves required will be 2, 2 and 1 respectively.
 So, the time taken will be 2.

Explanation 2:
 Assign the mouse at position -2 to -6.
 The number of moves required will be 4.
 So, the time taken will be 4.

"""


class Solution:
    def mice(self, A, B):
        # Sort the positions of mice and holes
        A.sort()
        B.sort()

        # Initialize the answer variable to negative infinity
        ans = float('-inf')

        # Iterate over the positions of mice
        for i in range(len(A)):
            # Calculate the absolute difference between the position of the current mouse and the corresponding hole
            diff = abs(A[i] - B[i])

            # Update the answer with the maximum difference encountered so far
            ans = max(ans, diff)

        # Return the maximum difference as the minimum time required
        return ans

"""
Intuition:
To minimize the time for the last mouse to get inside a hole, we need to assign each mouse to the closest available 
hole. By sorting the positions of mice and holes, we can match them up efficiently.

Time Complexity:
The time complexity of this solution is O(n log n) due to the sorting step, where n represents the number of mice 
(or holes). The iteration takes linear time, so it doesn't significantly affect the overall complexity.

Space Complexity:
The space complexity is O(1) as we don't use any extra space that grows with the input size. 
We only store the maximum difference in the ans variable, regardless of the input length.
"""