"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find the Kth Largest Element in a Stream


Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:
1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""


import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        heapq.heapify(self.pq)  # Create an empty min-heap

        n = len(nums)
        for i in range(n):
            heapq.heappush(self.pq, nums[i])  # Push elements into the min-heap
            if i > k - 1:
                heapq.heappop(self.pq)  # If heap size exceeds k, remove the smallest element

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)  # Push new value into the min-heap
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)  # If heap size exceeds k, remove the smallest element
        return self.pq[0]  # Return the smallest element in the min-heap

"""
# Intuition
We can efficiently find the kth largest element using a min-heap. By maintaining a min-heap of size k, we can track the 
kth largest elements seen so far.

# Approach
1. Initialize a min-heap with a size of k.
2. Iterate through the input array and add elements to the min-heap.
3. If the heap size exceeds k, remove the smallest element from the heap.
4. The top element of the min-heap will always represent the kth largest element.


# Complexity
- Time complexity:
O(n log k), where n is the number of elements in the input array. Each insertion and removal operation on the min-heap 
takes O(log k) time, and we perform these operations for n elements.

- Space complexity:
O(k), as we maintain a min-heap of size k.

"""