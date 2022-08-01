# Problem Description
# Given an integer A, you have to tell whether it is a prime number or not.
# A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
#
# Problem Constraints: 1 <= A <= 106
#
# Input Format: First and only line of the input contains a single integer A.
#
# Output Format: Print YES if A is a prime, else print NO.
#
# Example Input
# Input 1: 3
# Input 2: 4
#
#
# Example Output
# Output 1: YES
# Output 2: NO
#
# Example Explanation
# Explanation 1: 3 is a prime number as it is only divisible by 1 and 3.
# Explanation 2: 4 is not a prime number as it is divisible by 2.

def main():
    raw_input = int(input())
    input_range = int(raw_input ** (1 / 2))
    flag = "NO"  # default flag value

    for i in range(2, input_range):
        if raw_input % i == 0:
            flag = "NO"
            break
        else:
            flag = "YES"

    print(flag)
    return 0


if __name__ == '__main__':
    main()

