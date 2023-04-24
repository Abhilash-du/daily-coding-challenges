"""
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

"""
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max-heap by negating the weight of each stone in the input list
        p_queue = [-stone for stone in stones]

        # Rearrange the list into a heap structure
        heapq.heapify(p_queue)

        # Continue until there is only one or zero stone left in the heap
        while len(p_queue) > 1:
            # Remove the two largest stones from the heap
            first_stone, second_stone = heapq.heappop(p_queue), heapq.heappop(p_queue)

            # If both stones are not of the same weight, smash them together and add the resulting stone to the heap
            if first_stone != second_stone:
                heapq.heappush(p_queue, first_stone - second_stone)

        # If there is at least one stone left in the heap, return its weight. Otherwise, return 0
        return -p_queue[0] if p_queue else 0


"""
The time complexity (TC) of the given program is O(N log N), where N is the number of stones in the input list 
stones. This is because creating the initial priority queue and heapifying it both take O(N) time. Then, 
in each iteration of the while loop, we perform two heappop() operations (O(log N)) and at most one heappush() 
operation (O(log N)). Since we repeat the while loop until there is only one or zero stone left in the heap, 
the total number of iterations of the loop is O(N), resulting in a TC of O(N log N).

The space complexity (SC) of the program is O(N), where N is the number of stones in the input list stones. This is 
because we create a priority queue of size N (by negating the weight of each stone in the input list), and we also 
store the two largest stones in each iteration of the while loop, which takes up constant space. Thus, the overall 
space used by the program is O(N).
"""
