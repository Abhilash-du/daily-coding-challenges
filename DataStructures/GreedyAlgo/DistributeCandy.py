# Problem Description
# N children are standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum number of candies you must give?
#
# Problem Constraints
# 1 <= N <= 10**5
# -109 <= A[i] <= 10**9
#
# Input Format
# The first and only argument is an integer array A representing the rating of children.
#
# Output Format
# Return an integer representing the minimum candies to be given.
#
# Example Input
# Input 1: A = [1, 2]
# Input 2: A = [1, 5, 2, 1]
#
# Example Output
# Output 1: 3
# Output 2: 7
#
# Example Explanation
# Explanation 1:
#  The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot get 1 candy as 1 is its neighbor.
#  So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.
#
# Explanation 2:  Candies given = [1, 3, 2, 1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        LA = [1 for _ in range(n)]
        for i in range(1, n):
            # minimum candies from left
            if A[i - 1] < A[i]:
                LA[i] = LA[i - 1] + 1
        RA = [1 for _ in range(n)]

        for j in range(n - 2, -1, -1):
            # minimum candies from right
            if A[j + 1] < A[j]:
                RA[j] = RA[j + 1] + 1
        sum_val = 0
        for i in range(n):
            # total sum of candy to each person
            sum_val += max(LA[i], RA[i])
        return sum_val

# Solution Approach:-
# Greedy will work here ( Think of a supportive proof as an assignment ).
# Start with the guy with the least rating. Obviously, he will receive one candy.
#
# If he did receive more than one candy, we could lower it to 1 as none of the neighbors have a higher rating. Now,
# let us move to the one which is the second least. If the least element is its neighbor, then it receives two
# candies, else we can get away with assigning it just one candy.
#
# We keep repeating the same process to arrive at the optimal solution.
