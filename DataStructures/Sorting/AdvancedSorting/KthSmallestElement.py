"""
Q2. Kth Smallest Element
Problem Description: Find the Bth smallest element in given array A .
NOTE: Users should try to solve it in less than equal to B swaps.

Problem Constraints
1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 109

Input Format
The first argument is an integer array A.
The second argument is integer B.

Output Format
Return the Bth smallest element in given array.

Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3

Input 2:
A = [1, 2]
B = 2

Example Output:-
Output 1: 2
Output 2: 2

Example Explanation:-
Explanation 1: 3rd element after sorting is 2.
Explanation 2: 2nd element after sorting is 2.
"""
class Solution:
    # Function to find the Bth smallest element in the array A using less than or equal to B swaps
    # @param A: list of integers
    # @param B: integer representing the Bth position to find the element
    # @return an integer, the Bth smallest element
    def kthsmallest(self, A, B):
        A = list(A)  # Convert the input tuple A into a list

        n = len(A)  # Get the length of the list

        # The main loop to find the Bth smallest element using a variation of the selection sort algorithm
        for i in range(n - 1):
            min_indx = i  # Assume the current index i as the minimum index

            # Inner loop to find the actual minimum index among the unsorted part of the list
            for j in range(i + 1, n):
                if A[j] < A[min_indx]:
                    min_indx = j

            # Swap the minimum element with the first element of the unsorted part of the list
            A[i], A[min_indx] = A[min_indx], A[i]

            # If the current index i is equal to B, it means we found the Bth smallest element
            # Therefore, we can stop the sorting process prematurely to achieve the required number of swaps
            if i == B:
                break

        return A[B - 1]  # Return the Bth smallest element (B-1 index since indexing starts from 0)

"""
Intuition: The code uses a variation of the selection sort algorithm to find the Bth smallest element in the array 
A. It sorts the array in ascending order and stops the sorting process prematurely when the current index i is equal 
to the target index B. This ensures that the Bth smallest element is found using less than or equal to B swaps. As 
the code performs swaps, it builds a sorted prefix of the array, and when the Bth position is reached, 
the Bth smallest element is found at that position.

Time Complexity (TC):
The time complexity of the provided code is O(n * B), where n is the length of the array A and B is the target index to
 find the Bth smallest element. In the worst case, where B is close to n (but not exceeding 500 as specified in the
  problem constraints), the outer loop might run almost n times. For each iteration of the outer loop, the inner loop
   runs n - i times, resulting in B * (n + n-1 + n-2 + ... + 1) comparisons. Since the inner loop does not always run
    to completion due to the early stopping condition, the number of comparisons is effectively less than the maximum
     possible.

However, it's important to note that B is limited to a maximum of 500 in the problem constraints, which means the actual
 number of swaps and comparisons made by the algorithm is relatively small. Hence, in practice, the code might perform
  better than its worst-case time complexity suggests.

Space Complexity (SC):
The space complexity of the code is O(n) because it converts the input tuple A into a list, which requires additional
 memory proportional to the size of the input array. The sorting process is done in-place without using any additional
  data structures, so the overall space complexity is dominated by the input array.
"""