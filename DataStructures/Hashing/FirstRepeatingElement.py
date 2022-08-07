# Problem Description
# Given an integer array A of size N, find the first repeating element in it.
# We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
# If there is no repeating element, return -1.
#
# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 109
#
# Input Format: The first and only argument is an integer array A of size N.
#
# Output Format: Return an integer denoting the first repeating element.
#
#
#
# Example Input
# Input 1:
#  A = [10, 5, 3, 4, 3, 5, 6]
#
# Input 2:
#  A = [6, 10, 5, 4, 9, 120]
#
# Example Output
# Output 1:  5
# Output 2:  -1
#
# Example Explanation
# Explanation 1:  5 is the first element that repeats
# Explanation 2:  There is no repeating element, output -1
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Initialize index of first repeating element
        first_repeating_element = -1

        # Creates an empty hashset
        freq_hashmap = {}

        for i in range(n - 1, -1, -1):
            key = A[i]
            # checking if key is not present in hashmap
            if key not in freq_hashmap.keys():
                freq_hashmap[key] = 1  # if key present, add 1 in hashmap
            else:
                first_repeating_element = key  # if key is already present, means it is a repeating element

        return first_repeating_element

# For execution purpose:-
# A = [10, 5, 3, 4, 3, 5, 6]
# firstRepeatedElement = Solution()
# print(firstRepeatedElement.solve(A))
