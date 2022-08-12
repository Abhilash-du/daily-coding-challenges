# Problem Description
# Write a recursive function that, given a string S, prints the characters of S in reverse order.
#
# Problem Constraints: 1 <= |s| <= 1000
#
# Input Format: First line of input contains a string S.
#
# Output Format
# Print the character of the string S in reverse order.
#
# Example Input
# Input 1: scaleracademy
# Input 2: cool
#
# Example Output
# Output 1: ymedacarelacs
# Output 2: looc
#
# Example Explanation
# Explanation 1:Print the reverse of the string in a single line.
#
import sys

sys.setrecursionlimit(10 ** 6)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    str_val = input()
    printRev(str_val)
    return 0


def printRev(str_val):
    n = len(str_val)
    if n <= 0:
        return
    print(str_val[n - 1], end='')
    printRev(str_val[0:n - 1])


if __name__ == '__main__':
    main()

# Recursive function (printRev) takes string (S) as input and calls itself with next sliced string).
# example: hello can be called as o + reverse(hell)
# Recursion continues this way, when pointer reaches ‘\0’, all functions accumulated in stack print char at passed
# location (S) and print one by one.
#
# Time Complexity: O(n)
