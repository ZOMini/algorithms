# Очередь ограничена max размером.
# https://contest.yandex.ru/contest/23758/problems/I/
# I. Ограниченная очередь
class MyQueueSized:
    def __init__(self, max):
        self.queue = [None] * max
        self.max = max
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, x):
        if self.size != self.max:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max
            self.size += 1
            return 'push ok=)'
        return 'error'
        
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max
        self.size -= 1
        return x
    
    def peek(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        return x

test = MyQueueSized(2)
print (test.peek())
print (test.push(5))
print (test.push(2))
print (test.peek())
print (test.size)
print (test.size)
print (test.push(1))
print (test.size)
