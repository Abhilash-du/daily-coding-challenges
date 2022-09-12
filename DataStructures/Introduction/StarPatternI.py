# Problem Description
# Write a program to input an integer N from user and print
# hollow diamond star pattern series of N lines.
#
# See example for clarifications over the pattern.
#
# Problem Constraints
# 1 <= N <= 1000
#
# Input Format: First line is an integer N
#
# Output Format: N lines containing only char '*' as per the question.
#
# Example Input
# Input 1: 4
# Input 2: 6
#
# Example Output
# Output 1:-
# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********
#
# Output 2:-
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(n):
        space_req = i + i
        stars_req = (2 * n - space_req) // 2
        print("*" * stars_req + " " * space_req + "*" * stars_req)

    for i in range(n):
        i = n - i - 1
        space_req = i + i
        stars_req = (2 * n - space_req) // 2
        print("*" * stars_req + " " * space_req + "*" * stars_req)

    return 0


if __name__ == '__main__':
    main()
