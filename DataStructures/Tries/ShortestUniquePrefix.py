# Problem Description
# Given a list of N words, find the shortest unique prefix to represent each word in the list.
#
# NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible
#
#
#
# Problem Constraints
# 1 <= Sum of length of all words <= 106
#
#
#
# Input Format
# First and only argument is a string array of size N.
#
# Output Format
# Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.
#
# Example Input
# Input 1:  A = ["zebra", "dog", "duck", "dove"]
# Input 2:  A = ["apple", "ball", "cat"]
#
# Example Output
# Output 1:  ["z", "dog", "du", "dov"]
# Output 2:  ["a", "b", "c"]
#
# # Example Explanation
# Explanation 1:-
# Shortest unique prefix of each word is:
#  For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
#  For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
#  For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
#  For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog"
#
# Explanation 2:-
# "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent

class TriNode:
    def __init__(self, alphabet, isEnd=False):
        self.alphabet = alphabet
        self.childMap = {}
        self.isEnd = isEnd
        self.count = 0


class Tries:
    def __init__(self):
        self.root = TriNode("*")  # root will always starts with asterisk

    def insertWord(self, word):
        currNode = self.root  # starting the node with root (*)
        for alphabet in word:
            # iterating over each alphabet om the word
            if alphabet not in currNode.childMap:
                # if the alphabet is not the child of the parent, add it
                currNode.childMap[alphabet] = TriNode(alphabet)
            currNode = currNode.childMap[alphabet]
            currNode.count += 1  # increment count by one

    def findUniquePrefix(self, word):
        currNode = self.root
        prefix = ""
        for alphabet in word:
            # iterating over each alphabet in word
            currNode = currNode.childMap[alphabet]
            prefix += alphabet
            # checking if alphabet is child of the currentNode
            if currNode.count == 1:
                break
        return prefix


class Solution:
    def prefix(self, A):
        tries = Tries()  # creating tries object

        for word in A:
            # inserting each word in the tries
            tries.insertWord(word)
        # print(tries.childMap)
        ans = []
        for word in A:
            # finding prefix of each word
            ans.append(tries.findUniquePrefix(word))
        return ans

# Solution Approach:-
# input: ["zebra", "dog", "duck", "dot"]
#
# Now we will build prefix tree and we will also store count of characters
#
#                 root
#                 /|
#          (d, 3)/ |(z, 1)
#               /  |
#           Node1  Node2
#            /|        \
#      (o,2)/ |(u,1)    \(e,1)
#          /  |          \
#    Node1.1  Node1.2     Node2.1
#       | \         \            \
# (g,1) |  \ (t,1)   \(c,1)       \(b,1)
#       |   \         \            \
#     Leaf Leaf       Node1.2.1     Node2.1.1
#     (dog)  (dot)        \                  \
#                          \(k, 1)            \(r, 1)
#                           \                  \
#                           Leaf               Node2.1.1.1
#                           (duck)                       \
#                                                         \(a,1)
#                                                          \
#                                                          Leaf
#                                                          (zebra)
#
# Now, for every leaf / word , we find the character nearest to the root with frequency as 1.
# The prefix that the path from root to this character corresponds to, is the representation of the word.
