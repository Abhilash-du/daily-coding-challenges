"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the number of provinces

547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

"""
from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [-1 for _ in range(n)]  # Keep track of visited cities

        def bfs(city):
            q = deque([])  # Create a queue for BFS
            q.append(city)
            visited[city] = 1  # Mark current city as visited
            while q:
                curr_city = q.popleft()
                for adj_city in range(n):
                    # Check if the adjacent city is connected and not visited
                    if isConnected[curr_city][adj_city] == 1 and visited[adj_city] == -1:
                        visited[adj_city] = 1  # Mark adjacent city as visited
                        q.append(adj_city)

        provinces = 0  # Keep track of the number of provinces
        for city in range(n):
            if visited[city] == -1:
                bfs(city)  # Start BFS from unvisited city
                provinces += 1  # Increment the number of provinces

        return provinces

"""
## Approach and Intuition

To solve this problem, we can use a breadth-first search (BFS) approach. 
We start from each unvisited city and explore its connected cities.
If two cities are connected, we mark them as visited and continue the search. 
By doing so, we can identify all the provinces or groups of connected cities.

The time complexity of this approach is O(n^2), where n is the number of cities. 
This is because the BFS algorithm visits each city once. 

The space complexity is O(n) as we maintain a visited array of size n to keep track of visited cities.

## Time Complexity
O(n^2)

## Space Complexity
O(n)

"""