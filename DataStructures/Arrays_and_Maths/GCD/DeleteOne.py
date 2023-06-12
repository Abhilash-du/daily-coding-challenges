"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the max GCD after Delete one of the number from Array

Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor)
of the remaining array is maximum. Find the maximum value of GCD.

Problem Constraints
2 <= N <= 10^5
1 <= A[i] <= 10^9

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the maximum value of GCD.

Example Input:-
Input 1: A = [12, 15, 18]
Input 2: A = [5, 15, 30]

Example Output:-
Output 1: 6
Output 2: 15


Example Explanation:-

Explanation 1:
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.

Explanation 2:
 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Helper function to calculate the greatest common divisor (GCD)
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        n = len(A)

        # Calculate the prefix GCDs
        pre = [A[0]]
        for i in range(1, n):
            pre.append(gcd(pre[i - 1], A[i]))

        # Calculate the suffix GCDs
        suffix = [-1 for _ in range(n)]
        suffix[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = gcd(suffix[i + 1], A[i])

        ans = max(suffix[1], pre[n - 2])

        # Iterate through the array to find the maximum GCD
        for i in range(1, n - 1):
            if pre[i - 1] != suffix[i + 1]:
                ans = max(ans, gcd(pre[i - 1], suffix[i + 1]))
            else:
                ans = max(ans, pre[i - 1])

        return ans

"""
Intuition:
To find the maximum GCD, we calculate the prefix and suffix GCDs of the array elements. 
Then, we iterate through the array, considering each element as a potential candidate for deletion. 
Finally, we return the maximum GCD.

Time Complexity (TC):
The time complexity of this solution is O(N), where N is the size of the input array. 
This is because we iterate through the array twice to calculate the prefix and suffix GCDs, 
and then once more to find the maximum GCD.

Space Complexity (SC):
The space complexity of this solution is O(N) as well. We use two additional arrays, pre and suffix, 
to store the prefix and suffix GCDs respectively. Both arrays have a size of N, resulting in O(N) space complexity.

Feel free to add this code to your GitHub repository along with the intuition, time complexity, and 
space complexity explanations.
"""