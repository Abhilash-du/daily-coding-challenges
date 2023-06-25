"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine  minimum number of elements whose sign needs to be flipped such that
                the resultant sum is minimum non-negative.

Problem Description
Given an array Val of positive elements, you have to flip the sign of some of its elements such that the resultant
sum of the elements of array should be minimum non-negative(as close to zero as possible).
Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.

Problem Constraints
1 <= length of(Val) <= 100
Sum of all the elements will not exceed 10,000.

Input Format: First and only argument is an integer array Val.

Output Format: Return an integer denoting the minimum number of elements whose sign needs to be flipped.

Example Input
Input 1: Val = [15, 10, 6]
Input 2: Val = [14, 10, 4]

Example Output:-
Output 1: 1
Output 2: 1

Example Explanation:-
Explanation 1: Here, we will flip the sign of 15 and the resultant sum will be 1.
Explanation 2: Here, we will flip the sign of 14 and the resultant sum will be 0.
 Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there sign are not minimum.
"""
class Solution:
    def solve(self, Val):
        n = len(Val)
        target = sum(Val) // 2
        dp = [[(0, 0) for _ in range(target + 1)] for _ in range(n + 1)]

        # Finding the minimum number of elements required to achieve the target value
        for i in range(1, n + 1):
            for curr_target in range(1, target + 1):
                curr_element = Val[i - 1]
                if curr_element > curr_target:
                    # If the current element is greater than the target, it cannot be considered
                    dp[i][curr_target] = dp[i - 1][curr_target]
                else:
                    # The current element is less than or equal to the target, so it can be considered
                    consider = (curr_element + dp[i - 1][curr_target - curr_element][0],
                                1 + dp[i - 1][curr_target - curr_element][1])
                    not_consider = dp[i - 1][curr_target]

                    # Choosing the option with the minimum sum or, if sums are equal, the smaller count
                    if consider[0] > not_consider[0]:
                        dp[i][curr_target] = consider
                    elif consider[0] == not_consider[0] and consider[1] < not_consider[1]:
                        dp[i][curr_target] = consider
                    else:
                        dp[i][curr_target] = not_consider

        # Returning the count of elements needed to achieve the target sum
        return dp[n][target][1]


"""
# Problem Intuition:
Given an array, we need to flip the sign of some elements to minimize the sum of the array 
while keeping it non-negative. The problem can be solved using dynamic programming.

# Time Complexity Analysis:
The code uses a nested loop to iterate through the array and target sum. 
So, the time complexity is O(n * target), where n is the length of the array. 
With the given constraints, it performs efficiently.


# Space Complexity Analysis:
We use a 2D dp array to store intermediate results. Its size is (n+1) x (target+1), 
resulting in a space complexity of O(n * target). Considering the input constraints, it is within the acceptable range.
"""
