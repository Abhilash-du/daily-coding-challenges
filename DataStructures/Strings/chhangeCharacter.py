# Problem Description
# You are given a string A of size N consisting of lowercase alphabets.
#
# You can change at most B characters in the given string to any other lowercase alphabet such that the number of
# distinct characters in the string is minimized.
#
# Find the minimum number of distinct characters in the resulting string.
#
# Problem Constraints
# 1 <= N <= 100000
# 0 <= B < N
#
# Input Format
# The first argument is a string A.
# The second argument is an integer B.
#
# Output Format
# Return an integer denoting the minimum number of distinct characters in the string.
#
# Example Input
# A = "abcabbccd"
# B = 3
#
# Example Output
# 2
#
# Example Explanation
# We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
# So the minimum number of distinct character will be 2.

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freqArr = [0] * 26
        count = 0
        for char in A:
            idx = ord(char) - 97
            freqArr[idx] += 1
            if freqArr[idx] == 1:
                count += 1  # counting unique characters in the array
        freqArr.sort()
        for val in freqArr:
            if B - val >= 0 and val != 0:
                B -= val
                count -= 1
        return max(count, 1)

# Solution Approach/Observation:-
# Since there are 26 characters we can find frequency of each character.
# Sort them in ascending order. Since we have to minimize the number of distinct characters,
# we will change characters whose frequency is less into the character which has the highest frequency.
# We will check the maximum number of distinct characters we can successfully change.
