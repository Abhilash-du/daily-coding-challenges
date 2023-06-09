"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the number of selected batches

Problem Description

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people
i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations
 where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them.
So IB set criteria for selection: All those batches having strength at least D are selected.
Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then
    student x and student z will also know each other.



Problem Constraints
1 <= A <= 105
1 <= M <= 2*105
1 <= B[i] <= 104
1 <= C[i][0], C[i][1] <= A
1 <= D <= 109

Input Format
The first argument given is an integer A.
The second argument given is an integer array B.
The third argument given is a matrix C.
The fourth argument given is an integer D.

Output Format
Return the number of batches selected in IB.

Example Input
Input 1:
 A = 7
 B = [1, 6, 7, 2, 9, 4, 5]
 C = [  [1, 2]
        [2, 3]
       `[5, 6]
        [5, 7]  ]
 D = 12

Input 2:
 A = 5
 B = [1, 2, 3, 4, 5]
 C = [  [1, 5]
        [2, 3]  ]
 D = 6


Example Output

Output 1: 2
Output 2: 1


Example Explanation:-
Explanation 1:

 Initial Batches :
    Batch 1 = {1, 2, 3} Batch Strength = 1 + 6 + 7 = 14
    Batch 2 = {4} Batch Strength = 2
    Batch 3 = {5, 6, 7} Batch Strength = 9 + 4 + 5 = 18
    Selected Batches are Batch 1 and Batch 2.

Explanation 2:
 Initial Batches :
    Batch 1 = {1, 5} Batch Strength = 1 + 5  = 6
    Batch 2 = {2, 3} Batch Strength = 5
    Batch 3 = {4} Batch Strength = 4
    Selected Batch is only Batch 1.
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

class Solution:
    def solve(self, A, B, C, D):
        # Initialize variables
        visited = set()
        graph = defaultdict(list)

        # Create adjacency list representation of the graph
        for x, y in C:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        def dfs(index):
            # Perform depth-first search to calculate batch strength
            if index in visited:
                return 0
            visited.add(index)
            batch_strength = B[index]

            # Traverse neighbors recursively and add their strengths to batch_strength
            for neighbor in graph[index]:
                batch_strength += dfs(neighbor)

            return batch_strength

        ans = 0
        for i in range(A):
            batch_strength = 0
            if i not in visited:
                if graph[i]:
                    # If the current student has neighbors, perform DFS to calculate batch strength
                    batch_strength = dfs(i)
                else:
                    # If the current student has no neighbors, their individual strength is the batch strength
                    batch_strength = B[i]

            # Check if the batch strength meets the selection criteria
            if batch_strength >= D:
                ans += 1

        return ans
"""
Intuition:
- The problem is to select batches from the given students' information such that the batch strength 
    meets the given criteria.
- We represent the student relations using an adjacency list graph structure.
- We use depth-first search (DFS) to calculate the strength of each batch.
- We initialize a set to keep track of visited students.
- For each unvisited student, we start DFS to calculate the batch strength.
- The DFS function recursively visits the neighbors of a student, adds their strengths to the batch strength, 
    and marks them as visited.
- After calculating the batch strength, we check if it meets the selection criteria and increment the count of selected
   batches.
- Finally, we return the count of selected batches.

Time Complexity (TC): O(A + M)
- A is the number of students and M is the number of student relations.
- Creating the adjacency list takes O(M) time.
- DFS is performed at most A times (for each unvisited student).
- Each DFS visit takes O(M) time in the worst case (when the entire graph is visited).
- Thus, the overall time complexity is O(A + M).

Space Complexity (SC): O(A + M)
- Additional space is used to store the visited set and the adjacency list graph.
- The visited set can contain at most A elements (students).
- The adjacency list requires O(M) space to store the relations.
- Hence, the overall space complexity is O(A + M).
"""
