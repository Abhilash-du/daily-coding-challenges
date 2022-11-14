# Problem Description
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
#
# Problem Constraints
# 0 <= |intervals| <= 105
#
# Input Format
# First argument is the vector of intervals
# second argument is the new interval to be merged
#
# Output Format
# Return the vector of intervals after merging
#
# Example Input
# Input 1: Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
# Input 2: Given intervals [1, 3], [6, 9] insert and merge [2, 6] .
#
# Example Output
# Output 1:  [ [1, 5], [6, 9] ]
# Output 2:  [ [1, 9] ]
#
# Example Explanation
# Explanation 1: (2,5) does not completely merge the given intervals
# Explanation 2: (2,6) completely merges the given intervals

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        ans = []
        flag_found = False
        n = len(intervals)
        for i in range(n):
            if newInterval.end < intervals[i].start:
                # checking if new interval is already ended
                ans.append(newInterval)
                k = i
                while k < n:
                    # append other intervals
                    ans.append(intervals[k])
                    k += 1
                return ans
            elif newInterval.start < intervals[i].end:
                # if new interval is started before old interval ends
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
            else:
                ans.append(intervals[i])
        ans.append(newInterval)
        return ans

# Approach Followed/Observation:-
# This problem has a lot of corner cases that need to be handled correctly.
#
# Let us first talk about the approach.
# Given all the intervals, you need to figure out the sequence of intervals that intersect with the given new interval.
#
# Lets see how we check if interval 1 (a,b) intersects with interval 2 (c,d):
#
# Overlap case :
#
#     a---------------------b                      OR       a------b
#                 c-------------------d                c------------------d
# Non-overlap case:
#
#     a--------------------b   c------------------d
# Note that if max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.
#
# Once we figure out the intervals ( interval[i] to the interval[j] ) which overlap with the new interval,
# note that we can replace all the overlapping intervals with one interval, which would be
#
# (min(interval[i].start, newInterval.start), max(interval[j].end, newInterval.end)).
# ################################################################################################
# Following corner cases needs to be handled:-
# 1) Size of interval array as 0.
#
# 2) newInterval being an interval preceding all intervals in the array.
#
#     Given interval (3,6),(8,10), insert and merge (1,2)
# 3) newInterval being an interval succeeding all intervals in the array.
#
#     Given interval (1,2), (3,6), insert and merge (8,10)
# 4) newInterval not overlapping with any interval and falling in between 2 intervals in the array.
#
#     Given interval (1,2), (8,10) insert and merge (3,6)
# 5) newInterval covering all given intervals.
#
#     Given interval (3, 5), (7, 9) insert and merge (1, 10)
