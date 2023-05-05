"""

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the
Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of
the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party,
he can announce the victory and decide on the change in the game. Given a string senate representing each senator's
party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n
senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will
last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will
finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in round 1.
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.


Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.
"""
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Create two deques to store the index of senators from each party
        qr = deque([])
        qd = deque([])
        n = len(senate)

        # Add the index of senators to the appropriate deque based on their party
        for i in range(n):
            s_type = senate[i]
            if s_type == "R":
                qr.append(i)
            else:
                qd.append(i)

        # Perform the round-based procedure
        while qr and qd:
            r_index = qr.popleft()
            d_index = qd.popleft()

            # If the Radiant senator comes before the Dire senator, ban the next Dire senator's right
            # and add their index to the end of the Radiant deque
            if r_index < d_index:
                qr.append(r_index + n)
            # If the Dire senator comes before the Radiant senator, ban the next Radiant senator's right
            # and add their index to the end of the Dire deque
            else:
                qd.append(d_index + n)

        # If the Radiant deque still has senators with rights, they win. Otherwise, the Dire deque wins.
        return "Radiant" if len(qr) > 0 else "Dire"


"""
Approach:

1. Create two deques to store the index of senators from each party.
2. Add the index of senators to the appropriate deque based on their party.
3. Perform the round-based procedure until one party wins:
    --> If the Radiant senator comes before the Dire senator, ban the next Dire senator's right and add their index to
        the end of the Radiant deque.
    --> If the Dire senator comes before the Radiant senator, ban the next Radiant senator's right and add their index 
        to the end of the Dire deque.
4. If the Radiant deque still has senators with rights, they win. Otherwise, the Dire deque wins.


Time Complexity: O(n), where n is the length of the senate string. In the worst case, all senators have rights and 
the round-based procedure is repeated n/2 times.

Space Complexity: O(n), where n is the length of the senate string. We are storing the index of each senator in two 
deques.

"""
