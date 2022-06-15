# A. Дек
# id 65824578
# https://contest.yandex.ru/contest/23759/problems/A/
class Empty(Exception):
    # Если не нужно ни чего выводить после операции с нодом.
    # Можно было через None или как угодно, но сделал так.
    pass


class DeQueue:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_m = m
        self.head = 0
        self.tail = 0
        self.size = 0
        self.dictOfCommands = {
            'push_front': self._push_front,
            'push_back': self._push_back,
            'pop_front': self._pop_front,
            'pop_back': self._pop_back,
            }

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_m

    def push_back(self, x): # tail
        if self.is_full():
            raise IndexError
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_m
        self.size += 1
        raise Empty
    
    def push_front(self, x): # head
        if self.is_full():
            raise IndexError
        self.queue[self.head - 1] = x
        self.head = (self.head - 1) % self.max_m
        self.size += 1
        raise Empty
        
    
    def pop_front(self, *args): # head
        if self.is_empty():
            raise IndexError
        pop_elem = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_m
        self.size -= 1
        return pop_elem

    def pop_back(self, *args): # tail
        if self.is_empty():
            raise IndexError
        pop_elem = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_m
        self.size -= 1
        return pop_elem

    def _push_front(self, command):
        res = my_queue.push_front(command[1])
        return res

    def _push_back(self, command):
        res = my_queue.push_back(command[1])
        return res

    def _pop_front(self, command):
        res = my_queue.pop_front(command)
        return res

    def _pop_back(self, command):
        res = my_queue.pop_back(command)
        return res

    def execute(self, command):
        return self.dictOfCommands[command[0]](command)


# Не знаю туда ли копал, но познал многие радости Питона.
# В какой то момент код был на 200 строк.
# Словарь с командами/функциями дался оч. не легко.
# И есть четкое ощущение, что это можно сделать проще.
# Но это дает то, за чем мы все тут собрались, спасибо).
# Могу еще, если есть что.)

if __name__ == '__main__':
    num_commands = int(input()) # кол-во комманд
    num_nodes = int(input()) # кол-во ячеек
    my_queue = DeQueue(num_nodes)   
    result = []
    for _i in range(num_commands):
        command = input().split()
        try:
            com_arg = my_queue.execute(command)
            result.append(com_arg)
        except(IndexError):
            result.append('error')
        except(Empty):
            pass
    for _i in result:
        print (_i)
