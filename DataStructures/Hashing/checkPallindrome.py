# Problem Description
# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A
# such that it becomes a palindrome else return 0.
#
# Problem Constraints
# 1 <= |A| <= 105
#
# A consists only of lower-case characters.
#
# Input Format: First argument is an string A.
#
# Output Format: Return 1 if it is possible to rearrange the characters of the string A such that it
# becomes a palindrome else return 0.
#
# Example Input
# Input 1:  A = "abcde"
# Input 2:  A = "abbaee"
#
# Example Output
# Output 1:  0
# Output 2:  1
#
#
# Example Explanation
# Explanation 1:
#
#  No possible rearrangement to make the string palindrome.
# Explanation 2:
#
#  Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dict_val = {}
        n = len(A)
        if n == 1:
            return 1
        for i in A:  # Creating frequency hashmap for each elemebt
            if i in dict_val.keys():
                dict_val[i] = dict_val.get(i) + 1
            else:
                dict_val[i] = 1

        flag = 0
        one_count = 0
        for key in dict_val.keys():
            if one_count == 0 and n % 2 != 0 and dict_val[key] % 2 != 0:
                # if the length is odd means, there will be one odd value expected, will skip further checks
                one_count = 1
                continue
            if dict_val[key] % 2 == 0:  # checking for even count for each element
                flag = 1
            else:
                flag = 0
                break
        return flag

# Solution Approach followed:-
# Firstly we will create a frequency hashmap which will contain the count all the elements in the string
# Check for the count of each element,if count is even then palindrome can be created with the character (example:aabb)
# Also in case of odd length of string there will be one count of element odd example:nitin, here t occurs one time only
