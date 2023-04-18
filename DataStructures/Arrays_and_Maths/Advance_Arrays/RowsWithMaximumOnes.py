"""
Problem Description
Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.

NOTE:
If two rows have the maximum number of 1 then return the row which has a lower index.
Rows are numbered from top to bottom and columns are numbered from left to right.
Assume 0-based indexing.
Assume each row to be sorted by values.
Expected time complexity is O(rows + columns).


Problem Constraints
1 <= N <= 1000
0 <= A[i] <= 1

Input Format: The only argument given is the integer matrix A.

Output Format: Return the row with the maximum number of 1.

Example Input
Input 1:

 A = [   [0, 1, 1]
         [0, 0, 1]
         [0, 1, 1]   ]
Input 2:

 A = [   [0, 0, 0, 0]
         [0, 0, 0, 1]
         [0, 0, 1, 1]
         [0, 1, 1, 1]    ]


Example Output
Output 1: 0
Output 2: 3

Example Explanation
Explanation 1: Row 0 has maximum number of 1s.
Explanation 2: Row 3 has maximum number of 1s.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c = len(A[0]) - 1  # column value (to start with end of 0th row )
        row, ans = 0, 0  # row will start from zero and expecting ans as 0 initially
        while c >= 0 and row < len(A):
            # while column c is greater than or equal to zero and row doesn't exceeds max row index
            if A[row][c] == 0:
                # increment row and check for one in other row
                row += 1
            else:
                # if value found is one
                ans = row
                c -= 1
        return ans


"""
Here's a step-by-step explanation of the code:-

1. We initialize the column value c to the index of the last column in the first row (i.e., len(A[0]) - 1), 
   the row value row to 0, and the answer variable ans to 0.

2. We enter a while loop that continues until either c becomes negative (i.e., we have searched all columns), 
   or row exceeds the maximum row index (i.e., we have searched all rows).

3. Inside the loop, we check if the element at the current row row and column c is 0 or 1.

4. If it is 0, we move down to the next row by incrementing row.

5. If it is 1, we update ans to the current row row, since we have found a row with more 1's than any previous row. 
   We then move left to the next column by decrementing c.

6. Once the loop ends, we return the value of ans, which contains the row index with the maximum number of 1's.

The time complexity of the solution is O(rows + columns), since we search each row and column only once. 
The space complexity is O(1), since we only use a constant amount of extra space to store the loop variables and the 
answer variable.

"""
