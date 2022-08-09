# Problem Description
# Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if
# elements at those indices in the array are equal.
# Shaggy wants you to find a special pair such that the distance between that pair is minimum.
# Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.
#
# Problem Constraints
# 1 <= |A| <= 105
#
# Input Format: The first and only argument is an integer array A.
#
# Output Format: Return one integer corresponding to the minimum possible distance between a special pair.
#
# Example Input
# Input 1: A = [7, 1, 3, 4, 1, 7]
# Input 2: A = [1, 1]
#
# Example Output
# Output 1:  3
# Output 2:  1
#
# Example Explanation
# Explanation 1:-
# Here we have 2 options:
# 1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
# 2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
# Therefore the minimum possible distance is 3.
#
# Explanation 2: Only possibility is choosing A[1] and A[2].


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hmap_index = {}
        n = len(A)
        min_len = n + 1
        for i in range(n):
            key = A[i]
            if key in hmap_index.keys():
                start = hmap_index[key]  # if key is already present in hashmap means its repeating
                end = i
                min_len = min(min_len, end - start)  # getting the minimum length
            else:
                hmap_index[key] = i
            if min_len == n + 1:
                return -1
            return min_len



# Approach/Observation:-
# Idea behind this problem is to use hashing.
# Iterate over the the array and for each element if you found that element earlier also
# (i.e. stored in hash) then take the distance between them and update the hash with the
# current index.
# Answer will be minimum of all distances
# We are storing the most recent found index of each element because that will be the closest
# to the left of the next found index.