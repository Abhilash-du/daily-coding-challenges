"""
Q2. K Places Apart

Problem Description
N people having different priorities are standing in a queue.
The queue follows the property that each person is standing at most B places away from its position in the sorted queue.
Your task is to sort the queue in the increasing order of priorities.

NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity O(NlogB).

Problem Constraints
1 <= N <= 100000
0 <= B <= N

Input Format
The first argument is an integer array A representing the priorities and initial order of N persons.
The second argument is an integer B.

Output Format
Return an integer array representing the sorted queue.

Example Input
Input 1:
 A = [1, 40, 2, 3]
 B = 2

Input 2:
 A = [2, 1, 17, 10, 21, 95]
 B = 1

Example Output
Output 1: [1, 2, 3, 40]
Output 2: [1, 2, 10, 17, 21, 95]

Example Explanation
Explanation 1:
 Given array A = [1, 40, 2, 3]
 After sorting, A = [1, 2, 3, 40].
 We can see that difference between initial position of elements amd the final position <= 2.
Explanation 2:

 After sorting, the array becomes [1, 2, 10, 17, 21, 95].

"""

import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        pq = []  # Create an empty list to serve as a priority queue
        ans = []  # Create an empty list to store the answer
        heapq.heapify(pq)  # Convert the list into a heap (priority queue)
        n = len(A)  # Get the length of list A

        # Add the first B+1 elements of A to the priority queue
        for i in range(B + 1):
            heapq.heappush(pq, A[i])

        k = B + 1  # Set k to B+1 to start from the next element

        # Process the remaining elements of A
        while k < n:
            min_element = heapq.heappop(pq)  # Pop the smallest element from the priority queue
            heapq.heappush(pq, A[k])  # Push the next element from A to the priority queue
            ans.append(min_element)  # Add the popped element to the answer list
            k += 1  # Move to the next element

        # Process any remaining elements in the priority queue
        while pq:
            ans.append(heapq.heappop(pq))

        return ans
"""

Approach Followed:-

The given code implements a solution using a sliding window approach. Here's a breakdown of the approach:
The code initializes an empty priority queue (pq) using the heapify function from the heapq module. This priority queue 
will store the elements of the sliding window.

The code iterates over the first B+1 elements of the input list A and pushes them into the priority queue using the 
heappush function. This step ensures that the priority queue initially contains the smallest B+1 elements.

Next, the code sets the variable k to B+1, which represents the index from where we start processing the remaining 
elements of A.

The code enters a loop where it processes the remaining elements of A. In each iteration, it performs the following 
steps:

1. It pops the smallest element (min_element) from the priority queue using the heappop function.
2. It pushes the next element from A (at index k) into the priority queue using the heappush function.
3. It appends min_element to the ans list.
4. It increments k to move the sliding window by one position.
5. After processing all the elements of A in the loop, there might still be some remaining elements in the priority queue.
6. The code enters another loop to pop and append all the remaining elements to the ans list.

Finally, the ans list, containing all the elements from the sliding window in sorted order, is returned as the result.

The time complexity (TC) of this solution depends on the size of the input list A. The loop that processes the remaining
 elements of A runs n - (B + 1) times, where n is the length of A. Inside this loop, the operations of popping from the 
 priority queue (heappop) and pushing into the priority queue (heappush) both have a time complexity of O(log B). 
 Therefore, the overall time complexity of this solution is O((n - B - 1) * log B), 
 where n is the length of A and B is the given integer.

The space complexity (SC) of this solution is O(B) because the priority queue (pq) can store at most B + 1 elements. 
Additionally, the ans list will store the same number of elements. Therefore, the space complexity is linear with
 respect to B.

Note: The given code assumes that B is a valid index and doesn't perform any boundary checks.
"""