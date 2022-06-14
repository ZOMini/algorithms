# Стек + максимальное значение в стеке - O(1).
# G. Стек - MaxEffective
# https://contest.yandex.ru/contest/23758/problems/G/
class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if self.is_empty():
            print(None)
        else:
            max = sorted(self.items)
            print (max[len(self.items)-1])

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

test = Stack()
test.pop()
test.pop()
test.push(4)
test.push(-5)
test.push(7)
test.pop()
test.pop()
test.get_max()
test.pop()
test.get_max()
