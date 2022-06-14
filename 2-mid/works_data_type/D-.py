# Поиск индекса в связаном списке по значению
# D. Заботливая мама
# https://contest.yandex.ru/contest/23758/problems/D/
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def solution(node:Node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        else: 
            node = node.next_item
            idx += 1

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node3")
    print(idx)
    # result is idx == 2

test()
