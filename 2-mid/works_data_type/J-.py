# Очередь на списке
# https://contest.yandex.ru/contest/23758/problems/J/
# J. Списочная очередь
class MyQueueSized:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        return self.tail == 0
    
    def put(self, x):
        self.queue.append(x)
        self.tail += 1
        return f'put - {x}'

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.queue.pop(self.head)
        self.tail -= 1
        return x
    
    def size(self):
        return self.tail

test = MyQueueSized()
print(test.put (-34))
print(test.put (-23))
print(test.get())
print(test.size())
print(test.get())
print(test.size())
print(test.get())
print(test.get())
print(test.put (80))
print(test.size())
