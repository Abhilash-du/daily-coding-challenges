"""
You are given a floating-point number hour, representing the amount of time you have to reach the office.
To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of
 length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on
 the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach
 the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal
 point.

Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark.
    The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark.
    The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart.
    The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark.
    The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Constraints:
n == dist.length
1 <= n <= 10^5
1 <= dist[i] <= 10^5
1 <= hour <= 10^9
There will be at most two digits after the decimal point in hour.
"""
import math
from typing import List


class Solution:
    def minSpeedToArriveOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n > math.ceil(hour):
            return -1

        # Helper function to calculate the total time required to cover the distance at a given speed
        def totalTime(speed):
            time = 0
            for i in range(n - 1):
                time += math.ceil(dist[i] / speed)
            time += dist[n - 1] / speed
            return time

        left_speed = 1
        right_speed = 10 ** 7
        answer_speed = float('inf')

        # Binary search to find the minimum speed required
        while left_speed <= right_speed:
            current_speed = (left_speed + right_speed) // 2

            # Check if the total time at current speed is less than or equal to the given hour
            if totalTime(current_speed) <= hour:
                # It's able to cover within the specified hour, so we look for smaller speeds
                right_speed = current_speed - 1
                answer_speed = current_speed
            else:
                # A higher speed will be required to cover within the specified hour, so we look for larger speeds
                left_speed = current_speed + 1

        return answer_speed

"""
Intuition:
The problem requires finding the minimum positive integer speed (in kilometers per hour) that all the trains must travel
 at for you to reach the office on time. 
 To solve this, we use a binary search approach, searching for the minimum speed that can cover the total distance in 
 the given time.

Time Complexity (TC):
The time complexity of the binary search algorithm is O(log N), where N is the maximum possible speed
 (10^7 in this case). The totalDuration function has a time complexity of O(N) since it iterates over the distances. 
 So the overall time complexity is O(N log N).

Space Complexity (SC):
The space complexity is O(1) as the algorithm uses only a few extra variables and does not use any data structures 
that grow with the input size.

Note: The given constraints ensure that the answer will not exceed 10^7, and the hour will have at most two digits 
after the decimal point. Thus, the provided solution and approach should work efficiently within these limits.
"""