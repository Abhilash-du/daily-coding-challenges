"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the maximum and the minimum money that the ship company can earn

Problem Description
The local ship renting service has a special rate plan:

It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
The passengers buy tickets in turn, the first person in the queue goes first, then the second one, and so on up
to A-th person.
You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.

Problem Constraints
1 ≤ A ≤ 3000
1 ≤ B ≤ 1000
1 ≤ C[i] ≤ 1000
It is guaranteed that there are at least A empty seats in total.

Input Format
First argument is a integer A denoting the number of passengers in the queue.
Second arugument is a integer B deonting the number of ships.
Third argument is an integer array C of size B where C[i] denotes the number of empty seats in the i-th ship before the ticket office starts selling tickets.

Output Format
Return an array of size 2 denoting the maximum and minimum money that the ship company can earn.

Example Input:-
Input 1:
 A = 4
 B = 3
 C = [2, 1, 1]

Input 2:
 A = 4
 B = 3
 C = [2, 2, 2]

Example Output
Output 1: [5, 5]
Output 2: [7, 6]


Example Explanation
Explantion 1:
 Maximum money can be earned if the passenger choose : 2(first ship) + 1(first ship) + 1(second ship) + 1(third ship).
 So, the cost will be 5.
 Minimum money can be earned if the passenger choose : 1(senocd ship) + 2(first ship) + 1(first ship) + 1(third ship).
 So, the cost will be 5.

Explanation 2:
 Maximum money can be earned if the passenger choose : 2(first ship) + 2(second ship) + 2(third ship) + 1(first ship).
 So, the cost will be 7.
 Minimum money can be earned if the passenger choose : 2(senocd ship) + 2(first ship) + 1(first ship) + 1(second ship).
 So, the cost will be 6.

"""

import heapq


class Solution:
    def solve(self, A, B, C):
        # Create a max heap to keep track of ships with maximum vacant seats
        max_heap = [-val for val in C]
        heapq.heapify(max_heap)
        max_profit = 0

        # Create a min heap to keep track of ships with minimum vacant seats
        min_heap = C
        heapq.heapify(min_heap)
        min_profit = 0

        # Process each passenger in the queue
        for i in range(A):
            # Determine the ship with maximum vacant seats
            mx_val = -heapq.heappop(max_heap)  # Pop the largest negative value (largest absolute value)
            max_profit += mx_val  # Increment the maximum profit by the ticket cost
            heapq.heappush(max_heap, -(mx_val - 1))  # Push the updated vacant seats count to the max heap

            # Determine the ship with minimum vacant seats
            min_val = heapq.heappop(min_heap)  # Pop the smallest value
            min_profit += min_val  # Increment the minimum profit by the ticket cost
            if min_val > 1:
                heapq.heappush(min_heap, min_val - 1)  # Push the updated vacant seats count to the min heap

        return [max_profit, min_profit]


"""
Intuition:
The code aims to determine the maximum and minimum profit that a ship company can earn 
when selling tickets to passengers.
It uses two heaps, a max heap, and a min heap, to keep track of ships with maximum and minimum 
vacant seats respectively.

The max heap helps maximize the profit by selecting ships with the most vacant seats, while the min heap helps
minimize the profit by selecting ships with the least vacant seats.

Time Complexity (TC):
The time complexity of the solve() function is O(A * log(B)), 
where A represents the number of passengers and B represents the number of ships.
This is because for each passenger, the code performs heap operations, which take logarithmic time.

Space Complexity (SC):
The space complexity of the solve() function is O(B), where B represents the number of ships.
This is because the code uses two heaps, max_heap and min_heap, to store the vacant seat counts for each ship.

"""
