# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    first = None
    second = None
    prev = None

    def recoverTree(self, A):
        if A is None:
            return
        self.recoverTree(A.left)
        if self.prev is not None and self.prev.val > A.val:
            if self.first is None:
                self.first = self.prev.val
                self.second = A.val
            else:
                self.second = A.val
        self.prev = A
        self.recoverTree(A.right)
        return [self.second, self.first]

# Solution Approach/ Observation:-
# Let’s look at the inorder traversal of the tree. In the ideal case, the inorder
# traversal should be sorted. But in this case, because of the swapping 2 cases might arise : 1) A sequence like {1,
# 4, 3, 7, 9}, where the swapped pair are adjacent to each other. Only one inversion ( Inversion here means pair of
# integer A[i], A[i+1] where A[i] > A[i+1] ). 2) A sequence like {1, 9, 4, 5, 3, 10} where the swapped pair are not
# adjacent. 2 inversions. We take the min and max of the inversion numbers, and we know the number we need to swap to
# get the right answer.
