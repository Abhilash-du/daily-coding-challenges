"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:
1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""


class Solution:
    def arraySign(self, nums) -> int:
        # Initialize a variable to keep track of the number of negative values
        neg_count = 0

        # Loop through each value in the array
        for val in nums:
            # If the value is negative, increment the negative count
            if val < 0:
                neg_count += 1
            # If the value is 0, return 0 since the product will be 0
            elif val == 0:
                return 0

        # If the number of negative values is even, the product will be positive
        # Otherwise, the product will be negative
        return 1 if neg_count % 2 == 0 else -1

"""
Approach Followed:-
The approach used in this solution is quite simple. We loop through the given array nums and keep track of the 
number of negative values in the array using a variable neg_count. If we encounter a negative value, we increment 
neg_count. If we encounter a zero, we immediately return 0 since the product of any number and 0 is 0.

Once we have looped through the entire array, we check the value of neg_count. If it is even, then the product of all 
the values in the array is positive. If it is odd, then the product of all the values in the array is negative.

The time complexity of this solution is O(n), where n is the length of the input array nums, since we loop through 
the entire array once. 

The space complexity is O(1), since we only use a constant amount of extra space to store the 
neg_count variable.
"""