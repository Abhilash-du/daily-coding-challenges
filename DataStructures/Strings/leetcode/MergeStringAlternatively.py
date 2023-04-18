# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the
# merged string.
#
# Return the merged string.
#
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
# Constraints:-
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        n = max(w1, w2)
        k = 0
        ans = ""

        while k < n:
            if k < w1:
                ans += word1[k]
            if k < w2:
                ans += word2[k]
            k += 1
        return ans


'''
Approach Explained:-

The function first calculates the length of both input strings word1 and word2, and assigns it to variables w1 and 
w2 respectively. It then calculates the maximum length between the two input strings and assigns it to a variable n.

A variable k is initialized to zero, which will be used to iterate over the characters of both strings.

An empty string ans is also initialized, which will contain the final result.

The while loop iterates until k is less than n. Inside the loop, it checks if k is less than the length of word1 (
w1). If it is, it appends the kth character of word1 to the ans string. Similarly, if k is less than the length of 
word2 (w2), it appends the kth character of word2 to the ans string. The variable k is then incremented by 1 in each 
iteration.

Once the loop is finished, the function returns the final string ans.

Time complexity: The function contains a single while loop that iterates n times, where n is the maximum length 
between the two input strings. The operations inside the loop have constant time complexity. Therefore, 
the time complexity of the function is O(n).

Space complexity: The space complexity of the function is also O(n), as the length of the ans string can be at most n.
'''
