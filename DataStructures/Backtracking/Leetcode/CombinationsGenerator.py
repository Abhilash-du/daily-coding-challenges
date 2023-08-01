"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine possible combinations of k numbers chosen from the range [1, n].

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""


from typing import List

class CombinationsGenerator:
    def generate_combinations(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(start, remaining_elements, current_combination):
            # Base case: If we have selected k elements (remaining_elements == 0),
            # we have found a valid combination. Append a copy of current_combination to combinations.
            if remaining_elements == 0:
                combinations.append(current_combination.copy())
                return

            # If there are no more elements left to select (remaining_elements == 0),
            # or the current element (start) is greater than n,
            # we can't form any more combinations from this point, so return.
            if start > n:
                return

            # Include the current element (start) in the combination and move to the next one.
            current_combination.append(start)
            backtrack(start + 1, remaining_elements - 1, current_combination)

            # Exclude the current element (start) from the combination and move to the next one.
            current_combination.pop()
            backtrack(start + 1, remaining_elements, current_combination)

        # Start the recursive function with start=1 (as we need to consider integers from 1 to n).
        backtrack(1, k, [])
        return combinations


"""
Time Complexity (TC):
The number of combinations of k elements chosen from a set of n elements is given by the binomial coefficient C(n, k), 
which is defined as:  C(n, k) = n! / (k! * (n - k)!)
In the worst case scenario, we need to generate all possible combinations, and hence the number of recursive calls 
(time complexity) is equal to C(n, k). 
Therefore, the time complexity of the backtracking algorithm is O(C(n, k)) or O(n! / (k! * (n - k)!)).

While it's true that for small values of k, the time complexity might seem exponential (2^k) due to the binary branching
 factor in the recursion, the actual number of recursive calls is determined by the binomial coefficient, 
 which grows even faster.

Space Complexity (SC):
The recursion depth in the backtracking algorithm can go up to k, so the maximum space used by the recursion stack is 
O(k).
The space required to store the valid combinations is proportional to the number of valid combinations, 
which is C(n, k). The space needed is O(k * C(n, k)), but since C(n, k) dominates the space complexity, 
it is O(C(n, k)).
Therefore, the space complexity is also factorial, which is proportional to the number of valid combinations.
"""