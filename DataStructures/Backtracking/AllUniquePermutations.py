"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description:  Python solution to determine All Unique Permutations

Problem Description
Given an array A of size N denoting collection of numbers that might contain duplicates,
 return all possible unique permutations.
NOTE: No 2 entries in the permutation sequence should be the same.

Problem Constraints
1 <= |A| <= 9
0 <= A[i] <= 10

Input Format
Only argument is an integer array A of size N.

Output Format
Return a 2-D array denoting all possible unique permutation of the array.

Example Input
Input 1: A = [1, 1, 2]
Input 2: A = [1, 2]

Example Output
Output 1:
[ [1,1,2]
  [1,2,1]
  [2,1,1] ]

Output 2:
[ [1, 2]
  [2, 1] ]

Example Explanation
Explanation 1: All the possible unique permutation of array [1, 1, 2].
Explanation 2: All the possible unique permutation of array [1, 2].
"""
from collections import Counter


class Solution:
    def permute(self, A):
        """
        Generates all possible unique permutations of an array.

        Parameters:
            A (list): Input array of integers.

        Returns:
            list: List of lists representing unique permutations.
        """
        # Convert A to a list and create a counter to track the count of each element
        A = list(A)
        element_count = Counter(A)

        # List to store the resulting permutations
        permutations = []

        # Recursive function to generate unique permutations
        def generateUniquePermutations(current_permutation):
            """
            Recursive function to generate unique permutations.

            Parameters:
                current_permutation (list): Current permutation being generated.
            """
            # If the current permutation has the same length as A, it is a valid permutation
            if len(current_permutation) == len(A):
                permutations.append(current_permutation.copy())
                return

            # Iterate over each element in the counter
            for num in element_count:
                # If the count of the element is 0, skip to the next iteration
                if element_count[num] < 1:
                    continue

                # Reduce the count of the element, add it to the current permutation
                element_count[num] -= 1
                current_permutation.append(num)

                # Recursively generate permutations with the updated current permutation
                generateUniquePermutations(current_permutation)

                # Restore the count of the element and remove it from the current permutation for backtracking
                element_count[num] += 1
                current_permutation.pop()

        # Start the recursive generation with an empty current permutation
        generateUniquePermutations([])

        return permutations


"""
Intuition:
1. The given problem can be solved using a backtracking approach.
2. We use a recursive function to generate all unique permutations of the given array.
3. To handle duplicate elements, we use a counter to keep track of the count of each element in the array.
4. We iterate over each element in the counter.
5. For each element, we reduce its count, add it to the current permutation, and make a recursive call to 
   generate permutations with the updated current permutation.
6. After the recursive call, we restore the count of the element and remove it from the current permutation for 
   backtracking.
7. The recursion continues until the current permutation has the same length as the original array, at which point it 
   is considered a valid permutation and added to the resulting permutations list.
8. Finally, we return the list of all unique permutations.

Time Complexity Analysis:
The time complexity of this solution is O(N!), where N is the length of the input array.
The worst case occurs when there are no duplicate elements, resulting in N! permutations.
However, if there are duplicate elements, the number of recursive calls is reduced due to the checks to avoid duplicates.

Space Complexity Analysis:
The space complexity of this solution is also O(N!), as the resulting permutations are stored in a list.
"""