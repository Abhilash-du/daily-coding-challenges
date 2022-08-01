# Problem Description
# Given an integer array A, find if an integer p exists in the array such that the number of integers greater
# than p in the array equals p.

# Problem Constraints
# 1 <= |A| <= 2*105
# 1 <= A[i] <= 107

# Input Format: First and only argument is an integer array A.

# Output Format: Return 1 if any such integer p is present else, return -1.

# Example Input:-
# Input 1:  A = [3, 2, 1, 3]
# Input 2:  A = [1, 1, 3, 3]


# Example Output
# Output 1:  1
# Output 2:  -1

# Example Explanation
# Explanation 1:  For integer 2, there are 2 greater elements in the array..
# Explanation 2:  There exist no integer satisfying the required conditions.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort(reverse=True)  # sorting the array in reverse order

        # checking the number of values greater than each index
        count = -1
        if A[0] == 0:
            count = 1
        for i in range(1, n):
            if count == 1:
                break
            if i == A[i] and A[i] != A[i - 1] and A[i] > 0:
                count = 1
                break
        return count


# this solution is solved using Carry forward technique

example_Arr = [0, -1, -2, -4, -6]
sol = Solution()
print(sol.solve(example_Arr))
