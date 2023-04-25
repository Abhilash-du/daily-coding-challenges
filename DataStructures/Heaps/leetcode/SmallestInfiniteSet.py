"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

--> SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
--> int popSmallest() Removes and returns the smallest integer contained in the infinite set.
--> void addBack(int num) Adds a positive integer num back into the infinite set,
      if it is not already in the infinite set.

Input:
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]

Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation:
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:
    def __init__(self):
        # Initialize the current value to 1 and the set of values to an empty set
        self.curr = 1
        self.set_val = set()

    def popSmallest(self) -> int:
        # If the set of values is not empty, remove and return the smallest value
        if self.set_val:
            min_val = min(self.set_val)
            self.set_val.remove(min_val)
            return min_val
        # If the set of values is empty, return the current value and increment it
        else:
            self.curr += 1
            return self.curr - 1

    def addBack(self, num: int) -> None:
        # If the current value is greater than the input value, add the input value to the set
        if self.curr > num:
            self.set_val.add(num)
        # Otherwise, increment the current value and add all missing values up to the input value to the set
        else:
            while self.curr < num:
                self.set_val.add(self.curr)
                self.curr += 1


"""
Approach Followed:-

This program implements a data structure that maintains a set of integers and supports two operations: 
popSmallest() and addBack(num). The data structure has the property that if an integer num is added to the set, 
all smaller integers that were not already in the set will be added automatically.

The popSmallest() method returns and removes the smallest integer in the set, or if the set is empty, returns the 
next smallest integer not already in the set. This is achieved by keeping track of a current value self.curr which 
starts at 1 and is incremented every time a new integer is added to the set. If the set is non-empty, the method 
simply removes and returns the smallest integer using the min() function. Otherwise, the method returns the current 
value and increments it to get the next smallest integer not already in the set.

The addBack(num) method adds an integer num to the set, along with all smaller integers that were not already in the 
set. This is achieved by comparing num to the current value self.curr. If num is less than or equal to self.curr, 
it is added to the set. Otherwise, a loop is used to add all missing integers up to num to the set, by incrementing 
self.curr and adding it to the set until self.curr reaches num.

The time complexity of the popSmallest() method is O(n) in the worst case, where n is the number of elements in the 
set, because it may need to search for the smallest element. In the best case, where the set is non-empty, 
the time complexity is O(1) because it simply needs to remove the smallest element using the min() function.

The time complexity of the addBack(num) method is O(log n) in the worst case, where n is the number of elements in 
the set, because it uses a set implementation based on a balanced binary search tree which has logarithmic time 
complexity for adding an element. In the best case, where num is already in the set or num is equal to self.curr, 
the time complexity is O(1) because it simply needs to check if num is already in the set.

The space complexity of the data structure is O(n), where n is the number of elements in the set, because it stores 
all the elements in the set.

"""
