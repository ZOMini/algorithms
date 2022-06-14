# Стек + максимальное значение в стеке.
# F. Стек - Max
# https://contest.yandex.ru/contest/23758/problems/F/
class Stack:
    def __init__(self):
        self.items = []
        self.max = 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            print(self.items.pop())

    def get_max(self):
        if len(self.items) == 0:
            print(None)
        else:
            max = 0
            for i in self.items:
                if i > max:
                    max = i
            print(max)

test = Stack()
test.push(1)
test.push(2)
test.get_max()
test.pop()
test.pop()
test.pop()
test.get_max()
