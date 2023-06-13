"""
Problem Description
Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it, then the magician will fill the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that the kid can eat in A units of time.

NOTE:
floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 10^9+7

Problem Constraints
1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 10^5

Input Format
The first argument is an integer A.
The second argument is an integer array B of size N.

Output Format
Return an integer denoting the maximum number of chocolates the kid can eat in A units of time.

Example Input:-
Input 1:
 A = 3
 B = [6, 5]

Input 2:
 A = 5
 B = [2, 4, 6, 8, 10]

Example Output:-
Output 1: 14
Output 2: 33

Example Explanations:-
Explanation 1:
 At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates.
 At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates.
 At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate.
 so, total number of chocolates eaten are 6 + 5 + 3 = 14

Explanation 2:
 Maximum number of chocolates that can be eaten is 33.

"""
import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        # Create a max heap with negative values of chocolates in bags
        temp = [-val for val in B]
        heapq.heapify(temp)
        ans = 0
        i = 0
        # Perform the operation A times or until there are no more chocolates or bags
        while temp and i < A:
            # Eat chocolates from the bag with the maximum number of chocolates
            val = heapq.heappop(temp)
            ans += (-1 * val)
            # Fill the bag with half the number of chocolates eaten
            heapq.heappush(temp, -(-val // 2))
            i += 1

        # Return the maximum number of chocolates eaten modulo 10^9 + 7
        return ans % (10 ** 9 + 7)

"""
Intuition:
The code uses a max heap to keep track of the bags with the maximum number of chocolates. 
In each iteration, the kid eats chocolates from the bag with the maximum number of chocolates and then the bag gets 
refilled with half the number of chocolates eaten. The process is repeated A times or until there are no more chocolates
 or bags available. Finally, the code returns the maximum number of chocolates eaten modulo 10^9 + 7.

Time Complexity:
The time complexity of the code is O(A log N), where A is the given units of time and N is the number of bags. 
In each iteration, we perform operations on the max heap, which takes O(log N) time for both popping 
and pushing elements. Since we iterate A times, the overall time complexity is O(A log N).

Space Complexity:
The space complexity of the code is O(N) because we store the chocolates in the max heap, 
which can have at most N elements, one for each bag. Additionally, we use a few extra variables, 
but their space requirements are negligible compared to the input size. Therefore, the overall space complexity is O(N).
"""