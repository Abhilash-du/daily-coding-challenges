"""
Q5. Pair Sum divisible by M
Problem Description
Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.
Since the answer may be large, return the answer modulo (109 + 7).

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10**9
1 <= B <= 10**6

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 2

Input 2:
 A = [5, 17, 100, 11]
 B = 28

Example Output
 Output 1: 4
Output 2: 1

Example Explanation 1:
 All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5).
 So total 4 pairs.
"""


class Solution:
    # The function takes in a list of integers A and an integer B as inputs
    # and returns an integer as output.
    # A is the list of integers in which we want to find pairs.
    # B is the integer which is used to form pairs.
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # MOD is the constant value used for taking the modulo of the answer
        MOD = (10 ** 9) + 7

        # ans stores the count of pairs that we find
        ans = 0

        # hmap is a dictionary that will store the remainders of the
        # numbers in A after dividing by B as keys and their frequencies as values
        hmap = {}

        # Loop over all the elements in A
        for val in A:
            # Calculate the remainder of val after dividing by B
            rem1 = val % B

            # Calculate the value that needs to be paired with val
            val_to_find = B - rem1

            # Check if there is a number in hmap that can form a pair with val
            if val_to_find in hmap and rem1 != 0:
                # If yes, add the frequency of that number to the answer
                ans += hmap[val_to_find]

            # Check if val itself can form a pair with some number
            elif rem1 == 0 and rem1 in hmap:
                # If yes, add the frequency of that number to the answer
                ans += hmap[0]

            # Add the remainder of val to hmap
            if rem1 in hmap:
                hmap[rem1] += 1
            else:
                hmap[rem1] = 1

        # Return the answer after taking the modulo with MOD
        return ans % MOD


"""
Approach Followed:-
Initialize ans and hmap (a dictionary) to 0. For each value val in A, calculate the remainder of val when divided 
by B and store it in a variable rem1. Calculate the value val_to_find as B - rem1. 

Check if val_to_find exists in the dictionary hmap and rem1 is not equal to 0. If yes, add the value of 
hmap[val_to_find] to ans. Check if rem1 is equal to 0 and if 0 is already present in hmap. 

If yes, add the value of hmap[0] to ans. Increment the value of hmap[rem1] if rem1 is already present in the dictionary,
otherwise add a new key-value pair with rem1 as key and 1 as value. 

Return ans modulo (10**9) + 7. Note that this approach handles the special case of rem1 being equal to 0 separately, 
because adding the value of hmap[val_to_find] to ans would result in incorrect counting of pairs in that case.

The time complexity (TC) of the given code is O(n), where n is the length of the input array A. This is because the 
code only iterates over the elements of the array once.

The space complexity (SC) of the code is also O(n), since the code uses a hashmap to store the frequency of 
remainders encountered so far. The maximum number of distinct remainders that can be encountered is B, so the size of 
the hashmap is at most B. However, in the worst case, all elements of A could have distinct remainders, which would 
result in a hashmap of size n.
"""
