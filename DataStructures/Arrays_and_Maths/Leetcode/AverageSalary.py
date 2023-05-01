"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:
3 <= salary.length <= 100
1000 <= salary[i] <= 10^6
All the integers of salary are unique.
"""


class Solution:
    def average(self, salary: List[int]) -> float:
        # Initialize variables for minimum and maximum salaries
        min_salary = float('inf')
        max_salary = -1

        # Calculate sum of all salaries
        sum_val = 0
        for val in salary:
            max_salary = max(max_salary, val)  # Update maximum salary if necessary
            min_salary = min(min_salary, val)  # Update minimum salary if necessary
            sum_val += val  # Add current salary to sum

        # Calculate average salary by subtracting minimum and maximum salaries and dividing by number of employees - 2
        n = len(salary)
        avg_salary = (sum_val - max_salary - min_salary) / (n - 2)

        # Return the average salary
        return avg_salary


"""
The approach followed for the problem is:-

Initialize a variable "sum_val" to 0, "min_salary" to infinity and "max_salary" to -1. Traverse through the array of 
salaries and find the minimum and maximum salaries. Keep adding each salary to "sum_val". Calculate the average of 
salaries excluding the minimum and maximum salaries by subtracting the minimum and maximum salaries from "sum_val" 
and dividing it by (n-2), where "n" is the length of the array. Return the average.

Time Complexity: O(n), where n is the length of the input array of salaries. 

Space Complexity: O(1), as we are not using any extra space other than the given input array.

"""