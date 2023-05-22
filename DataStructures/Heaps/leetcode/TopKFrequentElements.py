"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to return the k most frequent elements from an integer Array

📚 Problem: Top K Frequent Elements
Problem Description:-
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        # Count the frequency of each element
        count = Counter(nums)

        # Create a min heap of size k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Retrieve the k most frequent elements from the heap
        top_k = [num for freq, num in heap]

        return top_k


"""
🔑 Approach:
1️⃣ Count the frequency of each element in the given array using the Counter class from the collections module.
2️⃣ Create a min heap and iterate over the items in the frequency count.
3️⃣ Push each element and its frequency as a tuple into the heap.
4️⃣ If the size of the heap exceeds k, remove the element with the smallest frequency using heapq.heappop().
5️⃣ Retrieve the k most frequent elements from the heap and return them as the result.

💡 Time Complexity:
The time complexity of this approach is better than O(n log n), where n is the size of the input array.
Since we iterate over n elements and perform operations on a heap of size k, the overall time complexity is O(n log k).

💡 Space Complexity:
The space complexity is O(n) as we use a Counter to store the frequency of each element and a heap of size k.

"""