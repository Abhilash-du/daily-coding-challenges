# Problem Description
# Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a
# target score of A for himself.
# Initially, Alex's score was zero. Alex can double his score by doing a question, or Alex can seek help from Sam for
# doing questions that will contribute 1 to Alex's score. Alex wants his score to be precisely A.
# Also, he does not want to take much help from Sam.
#
# Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.
#
# Problem Constraints
# 0 <= A <= 10^9
#
# Input Format
# The only argument given is an integer A.
#
# Output Format
# Return the minimum number of times help taken from Sam.
#
# Example Input
# Input 1: A = 5
# Input 2: A = 3
#
# Example Output
# Output 1: 2
# Output 2: 2
#
# Example Explanation
# Explanation 1:
# Initial score : 0
# Takes help from Sam, score : 1
# Alex solves a question, score : 2
# Alex solves a question, score : 4
# Takes help from Sam, score: 5
#
# Explanation 2:
# Initial score : 0
# Takes help from Sam, score : 1
# Alex solves a question, score : 2
# Takes help from Sam, score : 3
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        while A > 0:
            if A % 2 == 1:
                count += 1  # counting set bits
            A = A >> 1  # division by 2
        return count

# Approach/Observation from problem:-
# Claim :The number of times we would require help from sam is the number of bits that are set in A.
#
# Lets try to build an intuition for this. Instead of going from 0 to A , we will go in the reverse direction
# i.e. from A to 0.
# First initialise a cnt variable to 0 which is the number of times we took help from sam.Now we would follow this
# approach until A becomes 0.
#
# If A is an even number we can divide it by 2
# otherwise if A is an odd number we can subtract 1 from it and increment the cnt.
#
# Since every time we divide by 2 if its an even number , it is same as doing a left shift. The number of times A
# would become odd is the number of set bits of A.
#
# Lets take an example to make this more clear:
#
# A=17
# 0) 17 ,cnt=0
# 1) 17 -> 16 , cnt=1
# 2) 16 -> 8 , cnt=1
# 3) 8 -> 4 , cnt=1
# 4) 4 -> 2 , cnt=1
# 5) 2 -> 1 , cnt=1
# 6) 1 -> 0 , cnt=2
#
# binary representation of 17 = 10001 , and we can see that the number of set bits is the same as cnt that we
# obtained in the above approach.
#
# Therefore it is enough to just find the number of set bits of A.
# Time Complexity : O( log(A) )
