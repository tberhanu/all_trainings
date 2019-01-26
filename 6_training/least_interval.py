""" https://leetcode.com/problems/task-scheduler/
It's not quite clear how the argument 'n' is used for the idle timing??????
"""
def leastInterval(tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        freq = dict(Counter(tasks))
        active = 0
        idle = -1

        while True:
            if sum(e for e in freq.values()) == 0:
                return active + min(idle, n)

            for k, v in freq.items():
                if v != 0:
                    freq[k] = freq[k] - 1
                    active = active + 1

            idle = idle + 1


tasks = ["A", "A", "A", "B", "B", "B"]
print(leastInterval(tasks, 0))

tasks = ["A","A","A","B","B","B"]
print(leastInterval(tasks, 2))
