# Last updated: 6/4/2025, 9:21:48 PM

class Solution(object):

    def maxProfitAssignment(self, difficulty, profit, worker):

        """

        :type difficulty: List[int]

        :type profit: List[int]

        :type worker: List[int]

        :rtype: int

        """

        # Pair each job's difficulty with its profit

        jobs = list(zip(difficulty, profit))

        # Sort jobs by difficulty and by profit descending for the same difficulty

        jobs.sort(key=lambda x: (x[0], x[1]))

        

        # Sort workers by their ability

        worker.sort()

        

        # Variables to keep track of maximum profit and current best profit

        max_profit = 0

        best_profit = 0

        job_index = 0

        

        for ability in worker:

            # Update the best profit the worker can get

            while job_index < len(jobs) and jobs[job_index][0] <= ability:

                best_profit = max(best_profit, jobs[job_index][1])

                job_index += 1

            # Add the best profit for this worker to the total profit

            max_profit += best_profit

            

        return max_profit

# Example usage

difficulty = [2, 4, 6, 8, 10]

profit = [10, 20, 30, 40, 50]

worker = [4, 5, 6, 7]

solution = Solution()

print(solution.maxProfitAssignment(difficulty, profit, worker))  # Output: 100

difficulty = [85, 47, 57]

profit = [24, 66, 99]

worker = [40, 25, 25]

print(solution.maxProfitAssignment(difficulty, profit, worker))  # Output: 0
   

    


