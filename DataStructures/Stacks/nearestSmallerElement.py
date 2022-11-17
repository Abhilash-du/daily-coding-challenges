# Problem Description:-
#
# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array
# such that the element has an index smaller than i.
# More formally, G[i] for an element A[i] = an element A[j] such that j is maximum possible AND j < i AND A[j] < A[i]
#
# Elements for which no smaller element exist, consider the next smaller element as -1.
#
# Problem Constraints
# 1 <= |A| <= 100000
# -109 <= A[i] <= 109
#
# Input Format
# The only argument given is integer array A.
#
# Output Format Return the integer array G such that G[i] contains the nearest smaller number than A[i]. If no such
# element occurs G[i] should be -1.
#
# Example Input
# Input 1:  A = [4, 5, 2, 10, 8]
# Input 2:  A = [3, 2, 1]
#
# Example Output
# Output 1:  [-1, 4, -1, 2, 2]
# Output 2:  [-1, -1, -1]
#
# Example Explanation
# Explanation 1:
# index 1: No element less than 4 in left of 4, G[1] = -1
# index 2: A[1] is only element less than A[2], G[2] = A[1]
# index 3: No element less than 2 in left of 2, G[3] = -1
# index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
# index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
#
# Explanation 2:
# index 1: No element less than 3 in left of 3, G[1] = -1
# index 2: No element less than 2 in left of 2, G[2] = -1
# index 3: No element less than 1 in left of 1, G[3] = -1

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        stack = [A[0]]
        ans = [-1]

        for i in range(1, n):
            while stack and stack[-1] >= A[i]:
                # pop all the elements from the stack greater than current element
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(A[i])
        return ans

# Observation / Solution Approach:-
# The naive solution would look something like this:-
#   for i = 0 to size(A):
#     G[i] = -1
#     for j = i - 1 to 0:
#         if A[j] < A[i]:
#             G[i] = j
#             break
# Now look at A[i-1]. All elements with index smaller than i - 1 and greater than A[i-1] are useless to us because
# they would never qualify for G[i], G[i+1], ...
#
# We know that we only need previous numbers in descending order using the above fact.
#
# The pseudocode would look something like this:
#
# 1) Create a new empty stack st
#
# 2) Iterate over array `A`, where `i` goes from `0` to `size(A) - 1`. a) We are looking for value just smaller than
# `A[i]`. So keep popping from `st` till elements in `st.top() >= A[i]` or st becomes empty. b) If `st` is non-empty,
# then the top element is our previous element. Else the previous element does not exist. c) push `A[i]` onto st
