"""
 When a process starts, it calls 'start' with processId and startTime.
 When the same process ends, it calls 'end' with processId and endTime.
  Prints the logs of this system sorted by the start time of processes in the below format 
  {processId} started at {startTime} and ended at {endTime}
"""
import heapq

class Logger:
    """
    Start: O(1)
    End: O(lgN)
    Print: O(K)
    create a hashmap to store the start time of a pid.
    When we call end, we get the start time of the pid from the hashmap and append it into the heap.
    """
    def __init__(self):
        self.store = {}
        self.heap = []
        
    def start(self, pid, ts):
        if pid not in self.store:
            self.store[pid] = ts
        
    def end(self, pid, ts):
        if pid in self.store:
            heapq.heappush(self.heap, (self.store[pid], ts, pid))
            del self.store[pid]
    
    def print(self):
        tmp = self.heap[:]
        
        while len(tmp) > 0:
            start, end, pid = heapq.heappop(tmp)
            
            print('{} started at {} and ended at {}'.format(pid, start, end))