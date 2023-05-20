"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
that there is no contradiction.



Example 1:
Input:
equations = [["a","b"],["b","c"]],
values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]],
values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]],
values = [0.5],
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):

        # Step 1: Construct adjacency list with weights
        adj_list = defaultdict(list)
        for (first, second), val in zip(equations, values):
            adj_list[first].append((second, val))
            adj_list[second].append((first, 1 / val))

        # Step 2: Perform DFS for each query
        def dfs(src, dst, visited_arr, adjc_list):
            if src == dst:
                return 1.0

            visited_arr.add(src)
            for neighbor, val in adjc_list[src]:
                if neighbor not in visited_arr:
                    ans = dfs(neighbor, dst, visited_arr, adjc_list)
                    if ans != -1.0:
                        return val * ans
            return -1.0

            # Step 3: Process queries and store results

        final_ans = []
        for A, B in queries:
            if A not in adj_list or B not in adj_list:
                final_ans.append(-1.0)
            else:
                visited = set()
                result = dfs(A, B, visited, adj_list)
                final_ans.append(result)

        return final_ans

"""
# Intuition
In this problem, we are given equations and their corresponding values, representing the ratio between variables. 
We need to evaluate division queries based on these equations. To solve this problem efficiently, 
we can use a Depth-First Search (DFS) approach.

# Approach
1. We will construct an adjacency list using the given equations and values. This adjacency list will represent the 
    variables and their ratios.
2. For each query, we will perform a DFS from the source variable to the destination variable. We will keep track of 
    the visited variables and the product of ratios.
3. If we reach the destination variable during the DFS, we will return the product of ratios as the result. 
    If the destination variable is not reachable, we will return -1.0 as the result.

# Complexity
- Time complexity:
The time complexity of this approach is O(N * Q), where N is the number of equations and Q is the number of queries. 
We perform a DFS for each query, and in the worst case, each query can visit all the variables in the equations.

- Space complexity:
The space complexity is O(N), where N is the number of equations. We use an adjacency list to store the variables and 
their ratios.

"""