# Problem Description
# Given an array of size N, find the majority element. The majority element is the element that
# appears more than floor(n/2) times.
# You may assume that the array is non-empty and the majority element always exists in the array.
#
# Problem Constraints
# 1 <= N <= 5*105
# 1 <= num[i] <= 109
#
# Input Format
# Only argument is an integer array.
#
# Output Format
# Return an integer.
#
# Example Input
# [2, 1, 2]
#
# Example Output
# 2
#
# Example Explanation
# 2 occurs 2 times which is greater than 3/2.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        min_val = -10 ** 9 + 7
        majority_ele = min_val
        freq = 0
        for curr_element in A:  # checking for majority element in Array,moore's voting algo
            if freq == 0:
                majority_ele = curr_element
                freq = 1
            elif curr_element == majority_ele:
                freq += 1
            else:
                freq -= 1
                if freq == 0:
                    majority_ele = min_val

        freq = 0
        for element in A:  # count majority element
            if majority_ele == element:
                freq += 1
        n = len(A)
        if freq > n / 2:
            return majority_ele
        else:
            return None

# Approach/Observation followed:-
# If we cancel out each occurrence of an element X with all the other elements that are different from X,
# then X will exist till the end if it is a majority element.
# Loop through each element and maintain a count of the element that has the potential of being the majority element.
#
# If the next element is the same, then increments the count, otherwise decrements the count.
# If the count reaches 0, then update the potential index to the current element and reset the count to 1.
