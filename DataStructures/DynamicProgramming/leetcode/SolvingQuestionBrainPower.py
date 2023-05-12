"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order
(i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will
earn you points i points but you will be unable to solve each of the next brainpower questions. If you skip question i,
 you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
* If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.

* If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be
unable to solve questions 2 and 3.

Return the maximum points you can earn for the exam.

Example 1:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

Example 2:
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.

Constraints:

1 <= questions.length <= 10^5
questions[i].length == 2
1 <= points i, brainpower i <= 10^5
"""


class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [-1 for _ in range(n)]  # Initialize the DP array with -1 for all indices
        return self.maxProblem(questions, 0, dp)  # Call the recursive function to calculate the maximum points

    def maxProblem(self, questions, indx, dp):
        if indx >= len(
                questions):  # Base case: if the index is greater than or equal to the length of questions, return 0
            return 0
        if dp[indx] != -1:  # If the current index has already been calculated, return the previously calculated value
            return dp[indx]

        bp = questions[indx][0]  # Get the base points for the current question
        skip = questions[indx][1] + 1  # Get the skip value for the current question

        # Calculate the points for taking the current question and skipping the next 'skip' questions
        con_indx = bp + self.maxProblem(questions, indx + skip, dp)

        # Calculate the points for skipping the current question
        n_con_indx = self.maxProblem(questions, indx + 1, dp)

        # Store the maximum points for the current index in the DP array
        dp[indx] = max(con_indx, n_con_indx)

        # Return the maximum points for the current index
        return dp[indx]

"""
The given code uses dynamic programming to solve the problem of finding the maximum number of points that can be 
earned by answering the questions in the given list.

The approach used is to define a recursive function called maxProblem, which takes the current question index, 
the list of questions, and the DP array as arguments. It returns the maximum number of points that can be earned by 
considering the current question and all subsequent questions.

The DP array is used to store the maximum number of points that can be earned starting from a particular question index.
 If the value for a particular index is already calculated, it is simply returned from the DP array 
 without recalculating it.

The time complexity of this code is O(N), where N is the number of questions in the given list.

The space complexity of this code is also O(N)
"""