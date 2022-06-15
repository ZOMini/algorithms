# B. Калькулятор
# id 65811796
# https://contest.yandex.ru/contest/23759/problems/B/
OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
    }

class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0    

    def push(self, x):
        self.size += 1
        self.items.append(x)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Попытка удалить несуществующий элемент.')
        self.size -= 1
        return self.items.pop()


def calculator(line):
    my_stack = Stack()
    for elem in line:
        if elem not in OPERATORS:
            my_stack.push(elem)
        else:
            el1, el2 = int(my_stack.pop()), int(my_stack.pop())
            my_stack.push(OPERATORS[elem](el2, el1))
    result = my_stack.pop()
    return result

if __name__ == '__main__':
    line = input().split()
    print(calculator(line))    

