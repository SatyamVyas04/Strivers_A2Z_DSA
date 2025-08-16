'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''


class Solution:
    def JobScheduling(self, Jobs, n):
        chart = [-1] * (n + 1)
        profit = 0
        done = 0
        jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)

        for job in jobs:
            p, d, i = job.profit, job.deadline, job.id
            for j in range(d, 0, -1):
                if chart[j] == -1:
                    chart[j] = i
                    done += 1
                    profit += p
                    break

        return [done, profit]

# Link: https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
