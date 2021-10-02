class MyQueue:

    def __init__(self):
        self.myqueue = []
        

    def push(self, x: int) -> None:
        self.myqueue.insert(0, x)
        

    def pop(self) -> int:
        if len(self.myqueue) > 0:
            a = self.myqueue[len(self.myqueue)-1]
            self.myqueue = self.myqueue[:len(self.myqueue)-1]
            return a
        else:
            return False
        

    def peek(self) -> int:
        if len(self.myqueue) > 0:
            return self.myqueue[-1]
        else:
            return False
        

    def empty(self) -> bool:
        if len(self.myqueue) == 0:
            return True
        else:
            return False
