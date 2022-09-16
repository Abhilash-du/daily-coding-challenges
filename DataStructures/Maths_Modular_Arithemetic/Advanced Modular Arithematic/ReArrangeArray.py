# Q1. Rearrange Array

# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
#
# Example:
#
# Input : [1, 0]
# Return : [0, 1]
# Lets say N = size of the array. Then, following holds true :
#
# All elements in the array are in the range [0, N-1]
# N * N does not overflow for a signed integer

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            new_val = A[A[i] % n] % n
            final_val = n * new_val + A[i]  # converting it to a*n+c
            A[i] = final_val
        for i in range(n):
            A[i] = A[i] // n  # getting the actual value
        return A

# Approach Followed:-
# The brute force way would be to create an extra array and append values to it based on the Arr[Arr[i]] value
# For brute force: TC: O(n) an SC: O(N)
#
# Since we have to complete using the same array as its mentioned expected SC: O(1)
# Now in order to use the same array, we will have to first create an array so that both values can be fetched.
# Logic: fetch the value that needs to be updated at current index and merge using below formula:-
#  A[i]= n*new_value+current_value
# Now for each row we can  iterate and update the value
# So now since we are main concerned with the new value, we can divide it by n (also to find old value: %n can be used)
# the final array created will contain all rearranged value  (TC: O(n)  and SC: O(1))
