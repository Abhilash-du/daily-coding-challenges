# Q4. N/3 Repeat Number
# Solved
# character background character
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array
# in linear time and constant additional space.
# If so, return the integer. If not, return -1.
#
# If there are multiple solutions, return any one.
#
# Problem Constraints
# 1 <= N <= 7*105
# 1 <= A[i] <= 109
#
# Input Format
# The only argument is an integer array A.
#
# Output Format
# Return an integer.
#
# Example Input
# [1 2 3 1 1]
#
# Example Output
# 1
#
# Example Explanation
# 1 occurs 3 times which is more than 5/3 times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        # n//3 means two values can be present in the list which has higher frequency
        num1 = -10 ** 7 + 1
        c_one = 0
        num2 = -10 ** 7 + 1
        c_two = 0

        for i in range(n):
            if A[i] == num1:
                c_one += 1
            elif A[i] == num2:
                c_two += 1
            elif c_one == 0:
                num1 = A[i]
                c_one += 1
            elif c_two == 0:
                num2 = A[i]
                c_two += 1
            else:
                c_one -= 1
                c_two -= 1

        num_list = [num1, num2]
        majority_flag = False
        # Check actual counts of candidates
        num=0
        for num in num_list:
            final_count = 0
            for item in A:
                if item == num:
                    final_count += 1
            if final_count > n // 3:
                majority_flag = True
                break

        if majority_flag:
            return num
        else:
            return -1

# Approach Followed:-
# It is important to note that if at a given time, you have 3 distinct element from the array,
# if you remove them from the array, your answer does not change.
#
# Assume that we maintain 2 elements’ counts as we traverse along the array.
#
# When we encounter a new element, there are 3 cases possible :
#
# We don’t have 2 elements yet. So add this to the list with count as 1.
#
# This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now. Removing
# them does not change the answer. So decrement 1 from count of 2 existing elements. If their count falls to 0,
# obviously its not a part of 2 elements anymore.
#
# The new element is same as one of the 2 elements. Increment the count of that element.
#
# Consequently, the answer will be one of the 2 elements left behind. If they are not the answer, there is no element
# with count > N / 3.
