"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine  all possible letter combinations that the number could represent

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        # If the input is empty, return an empty list.
        if n < 1:
            return []

        # Create a mapping of digits to their corresponding letters.
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # If the input has only one digit, return the corresponding letters.
        if n == 1:
            return list(hmap[digits])

        ans = []  # List to store the final combinations.

        # Helper function to perform backtracking and generate combinations.
        def backtrack(i, curr_str):
            if len(curr_str) == n:
                ans.append(curr_str)
                return

            # Get the letters corresponding to the current digit and explore each letter.
            for c in hmap[digits[i]]:
                backtrack(i + 1, curr_str + c)

        # Start the backtracking process from the first digit (index 0) with an empty string.
        backtrack(0, "")

        return ans
"""
Intuition:
The given problem can be solved using a recursive backtracking approach. We create a dictionary (hmap) to map each 
digit to its corresponding letters. We then start the backtracking process from the first digit (index 0) with an empty
 string. The recursive function explores all possible combinations of letters for each digit, eventually forming all 
 valid letter combinations. The final answer list contains all the possible letter combinations that the input string 
 of digits could represent.

Time Complexity:
The time complexity of the solution depends on the number of possible combinations. In the worst case, when each digit 
has the maximum number of corresponding letters (4 letters), the time complexity would be O(4^n), where n is the number
 of digits in the input string. This is because for each digit, we explore up to four possible letters. However, since
  the input has constraints (0 <= digits.length <= 4) and the number of possible combinations is relatively small, the 
  solution is efficient for practical purposes.

Space Complexity:
The space complexity of the solution is O(1) for the input as it does not consume any extra space based on the size of
 the input. The space complexity for the recursive stack is O(n), where n is the number of digits in the input string. 
 This is because the recursive function makes at most n recursive calls, and each call adds one digit to the current 
 string. Additionally, the space complexity for the answer list (ans) is also O(n), as in the worst case, there can be 
 up to 4^n possible combinations. However, since the number of possible combinations is relatively small (as explained
  earlier), the space complexity is manageable.
"""