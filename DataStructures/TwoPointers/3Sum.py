# Problem Description
# Given an array A of N integers, find three integers in A such that the sum is closest to a
# given number B. Return the sum of those three integers.
# Assume that there will only be one solution.
#
# Problem Constraints
# -10^8 <= B <= 10^8
# 1 <= N <= 10^4
# -10^8 <= A[i] <= 10^8
#
#
# Input Format
# First argument is an integer array A of size N.
#
# Second argument is an integer B denoting the sum you need to get close to.
#
# Output Format
# Return a single integer denoting the sum of three integers which is closest to B.
#
# Example Input
# Input 1:
# A = [-1, 2, 1, -4]
# B = 1
#
# Input 2:
#
# A = [1, 2, 3]
# B = 6
#
# Example Output
# Output 1: 2
# Output 2: 6
#
# Example Explanation
# Explanation 1:  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# Explanation 2:  Take all elements to get exactly 6.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        diff = float('inf')
        ans = -1
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                current_sum = A[i] + A[j] + A[k]
                if current_sum == B:
                    return current_sum
                if abs(current_sum - B) < diff:
                    diff = abs(current_sum - B)
                    ans = current_sum
                elif current_sum < B:
                    j += 1
                else:
                    k -= 1
        return ans

# Solution Approach/Observation:-
# We can sort the array
# When the array is sorted, try to fix the least integer by looping over it.
# Lets say the least integer in the solution is arr[i].
#
# Now we need to find a pair of integers j and k, such that arr[j] + arr[k] is closest to (target - arr[i]).
# To do that, let us try the 2 pointer approach.
# If we fix the two pointers at the end ( that is, i+1 and end of array ), we look at the sum.
#
# If the sum is smaller than the sum we need to get to, we increase the first pointer.
# If the sum is bigger, we decrease the end pointer to reduce the sum.
