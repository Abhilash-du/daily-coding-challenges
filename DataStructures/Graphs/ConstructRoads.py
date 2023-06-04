"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to Construct max Roads

Problem Description
A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads
 such that the new country formed remains bipartite country.
Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v)
that belongs to the country, u and v belong to different sets.
Also, there should be no multiple roads between two cities and no self loops.
Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.
NOTE: All cities can be visited from any city.

Problem Constraints
1 <= A <= 105
1 <= B[i][0], B[i][1] <= N

Input Format
First argument is an integer A denoting the number of cities, N.
Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads
i.e. there is a road between cities B[i][0] and B[1][1] .

Output Format
Return an integer denoting the maximum number of roads king can construct.

Example Input
Input 1:
 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]

Input 2:
 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]

Example Output
Output 1: 0
Output 2: 2

Example Explanations:-
Explanation 1: We can't construct any new roads such that the country remains bipartite.
Explanation 2: We can add two roads between cities (4, 2) and (4, 5).
"""
from collections import deque, defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        MOD = (10 ** 9) + 7
        bgraph = defaultdict(list)

        if A <= 1:
            return 0

        # Constructing the graph
        for road in B:
            bgraph[road[0]].append(road[1])  # Adding edges between cities
            bgraph[road[1]].append(road[0])  # Adding edges between cities

        q = deque([])
        q.append((B[0][0], 0))  # Starting BFS traversal from the first city with color 0

        set1 = 0
        set2 = 0
        visited = [-1 for _ in range(A + 1)]  # Keeps track of the color assigned to each city

        while q:
            top_city, color = q.popleft()

            if visited[top_city] == -1:
                for city in bgraph[top_city]:
                    q.append((city, color ^ 1))  # Flipping the color by using XOR operation
                    visited[top_city] = color  # Marking the city with its assigned color

        # Counting the number of cities in each set
        for i in range(1, A + 1):
            if visited[i] == 1:
                set1 += 1
            else:
                set2 += 1

        return ((set1 * set2) - (A - 1)) % MOD  # Calculating the maximum number of roads king can construct


"""
Intuition:
    We can solve this problem using a BFS approach.
    1. We construct a graph based on the given roads.
    2. Perform a BFS traversal, assigning colors to cities.
    3. Count the number of cities in each set.
    4. Calculate the maximum number of roads the king can construct using the set counts.
    5. Return the result % (10^9 + 7).

# Time Complexity (TC): O(E) - where E represents the number of edges (roads) in the graph.
# Space Complexity (SC): O(N) - where N represents the number of cities.
"""
