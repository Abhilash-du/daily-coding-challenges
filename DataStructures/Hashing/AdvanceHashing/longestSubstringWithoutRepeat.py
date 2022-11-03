# Problem Description
# Given a string A, find the length of the longest substring without repeating characters.
# Note: Users are expected to solve in O(N) time complexity.
#
# Problem Constraints
# 1 <= size(A) <= 106
#  String consists of lowerCase,upperCase characters and digits are also present in the string A.
#
# Input Format
# Single Argument representing string A.
#
# Output Format
# Return an integer denoting the maximum possible length of substring without repeating characters.
#
# Example Input
# Input 1:
#  A = "abcabcbb"
# Input 2:
#  A = "AaaA"
#
# Example Output
# Output 1:
#  3
# Output 2:
#   2
#
# Example Explanation
# Explanation 1:  Substring "abc" is the longest substring without repeating characters in string A.
# Explanation 2:  Substring "Aa" or "aA" is the longest substring without repeating characters in string A.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        hmap = {}
        l = 0
        r = 0
        n = len(A)
        ans = -10

        while r < n:
            if A[r] in hmap:
                while A[r] in hmap:
                    hmap.pop(A[l])  # removing elements from hmap
                    l += 1
            ans = max(ans, r - l + 1)
            hmap[A[r]] = r  # adding element in the hmap
            r += 1
        return ans

# Solution/Approach followed:-
# Idea is to have two indexes, l(left) and r(right), these two vars will be use to iterate through the string
# 1.We will create a hashmap to store each element(A[r]) until r reaches n-1 element
# 2. Each time we will check if the element A[r] is present in hmap
# 3. if A[r] is present means duplicate is found, so we will have to remove the same element which is there on left side
# 4. once the repeated element is removed from left(from hmap) then we will again increment r  and add values in hmap
# 5. In each iteration we will be checking the length and max value will always be picked up
