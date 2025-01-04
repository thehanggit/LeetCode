class MyStack:

    def __init__(self):
        self.queuein = deque()
        self.queueout = deque()

    def push(self, x: int) -> None:
        self.queuein.append(x)

    def pop(self) -> int:
        while self.queuein:
            self.queueout.append(self.queuein.popleft())
        return self.queueout.pop()

    def top(self) -> int:
        while self.queuein:
            self.queueout.append(self.queuein.popleft())
        return self.queueout[-1]

    def empty(self) -> bool:
        return not self.queuein and not self.queueout


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()