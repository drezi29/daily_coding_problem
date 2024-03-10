'''
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
'''

from dataclasses import dataclass


@dataclass
class Log:
    data : int
    previous : None

    def __init__(self, data : int):
        self.data = data


class LogsList:
    def __init__(self):
        self.last_log = None

    def record(self, new_log : Log):
        if self.last_log is None:
            self.last_log = new_log
        else:
            new_log.previous = self.last_log
            self.last_log = new_log
        return

    def get_last(self, n : int):
        log = self.last_log
        for i in range(n):
            log = log.previous
        return log
