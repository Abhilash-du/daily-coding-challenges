"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find the Maximum Subsequence Score

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k.
You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1}
by deleting some or no elements.

Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation:
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation:
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[j] <= 10^5
1 <= k <= n

"""

import heapq

class Solution:
    def maxScore(self, nums1, nums2, k: int) -> int:
        # Create pairs of corresponding elements from nums1 and nums2
        pairs = [(a, b) for a, b in zip(nums1, nums2)]

        # Sort the pairs based on the second element (nums2) in descending order
        pairs.sort(key=lambda x: -x[1])

        # Create a heap of the first k elements from pairs based on the first element (nums1)
        top_k_heap = [x[0] for x in pairs[:k]]

        # Calculate the sum of the elements in the heap
        top_k_sum = sum(top_k_heap)

        # Convert the list into a heap data structure
        heapq.heapify(top_k_heap)

        # Initialize the answer with the product of the sum and the kth element from pairs
        ans = top_k_sum * pairs[k - 1][1]

        # Iterate from k to the end of pairs
        for i in range(k, len(pairs)):
            # Remove the smallest element from the heap
            top_element = heapq.heappop(top_k_heap)

            # Update the sum by subtracting the removed element and adding the current element from pairs
            top_k_sum -= top_element
            top_k_sum += pairs[i][0]

            # Push the current element from pairs into the heap
            heapq.heappush(top_k_heap, pairs[i][0])

            # Update the answer if the product of the updated sum and the current element from pairs is larger
            ans = max(ans, top_k_sum * pairs[i][1])

        # Return the maximum score
        return ans


"""
## Problem: Maximum Score from Subsequence of Arrays

**Intuition:**
We are given two arrays, `nums1` and `nums2`, and we need to choose a subsequence of indices from `nums1` to maximize 
the score. The score is defined as the sum of selected elements from `nums1` multiplied by the minimum of the selected 
elements from `nums2`. To achieve the maximum score, we need to carefully select elements from both arrays.

**Approach:**
1. We create pairs of corresponding elements from `nums1` and `nums2` and sort these pairs based on `nums2` in 
  descending order. Sorting ensures that we prioritize selecting larger elements from `nums1`.
2. We maintain a heap, `top_k_heap`, to keep track of the top k elements from `nums1`. We initialize the heap with the 
  first k elements from `nums1`. We also calculate the sum, `top_k_sum`, of these elements.
3. We convert the `top_k_heap` list into a heap data structure using `heapify`.
4. We initialize the answer, `ans`, with the product of the sum (`top_k_sum`) and the kth element from pairs 
  (`pairs[k-1][1]`).
5. We iterate from k to the end of pairs:
     - Remove the smallest element from `top_k_heap` using `heappop`.
     - Update the sum (`top_k_sum`) by subtracting the removed element and adding the current element from pairs.
     - Push the current element from pairs into `top_k_heap` using `heappush`.
     - Update the answer (`ans`) if the product of the updated sum (`top_k_sum`) and the current element from pairs is 
        larger.
6. Finally, we return the maximum score, `ans`.

**Time Complexity:**
The time complexity of this approach is O(n log n), where n is the length of the arrays `nums1` and `nums2`. 
The main contributing factor is the sorting step when creating pairs based on `nums2`.

**Space Complexity:**
The space complexity is O(n), where n is the length of the arrays `nums1` and `nums2`. We store pairs of elements in the
 `pairs` list, and the `top_k_heap` heap occupies additional space.

"""