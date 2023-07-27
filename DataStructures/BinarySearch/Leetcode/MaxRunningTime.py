"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the Maximum running time for N computers

2141. Maximum Running Time of N Computers
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run
 a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given
 batteries.
Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can
remove a battery from a computer and insert another battery any number of times.
The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing
and inserting processes take no time.
Note that the batteries cannot be recharged.
Return the maximum number of minutes you can run all the n computers simultaneously.

Example 1:-
Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation:
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:-
Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation:
Initially, insert battery 0 into the first computer and battery 2 into the second computer.
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer.
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.


Constraints:
1 <= n <= batteries.length <= 10^5
1 <= batteries[i] <= 10^9
"""

from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Initialize the search range
        left, right = 1, sum(batteries) // n

        while left < right:
            # Calculate the mid-point of the search range
            target = right - (right - left) // 2

            # Calculate the total time that can be run with the current target power level
            total_time = 0
            for power in batteries:
                # Use min() to calculate the time considering the constraint of each battery's capacity
                total_time += min(power, target)

            if total_time // n >= target:
                # If the total time is greater than or equal to the target, we can try higher power levels
                left = target
            else:
                # If the total time is less than the target, we need to decrease the power level
                right = target - 1

        # Return the maximum achievable power level
        return left

"""
Intuition:

The problem can be solved using a binary search approach. We are looking for the maximum possible run time (power level)
 that allows all n computers to run simultaneously. We can use binary search to find the optimal power level efficiently.

Initially, we set the search range for the power level from 1 (minimum possible value) to the average battery time 
divided by the number of computers. This ensures that the total time with the average power level is close to evenly 
distributed among all computers.

We then repeatedly calculate the total time that can be run at the current power level by distributing each battery's 
time among the computers using the min() function. If the total time is greater than or equal to the target power level,
 we search for even higher power levels in the right half of the search range. Otherwise, we search for lower power 
 levels in the left half of the search range.

The binary search continues until the left and right pointers converge, and we find the maximum achievable power level.

Time Complexity (TC):
The binary search has a time complexity of O(log(max_battery_time * n)). Within each binary search iteration, 
we iterate through the batteries once to calculate the total time at the current power level, which takes O(n) time. 
Therefore, the overall time complexity is O(n log(max_battery_time * n)), where max_battery_time is the maximum battery
 time in the input.

Space Complexity (SC):
The space complexity is O(1) as we use a constant amount of extra space to store variables regardless of the input size.
"""