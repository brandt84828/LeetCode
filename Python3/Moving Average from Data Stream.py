class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.queue.popleft()
            self.queue.append(val)
        else:
            self.queue.append(val)
        return sum(self.queue)/len(self.queue)
