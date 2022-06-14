# Удаление Нода по индексу
# C. Нелюбимое дело
# https://contest.yandex.ru/contest/23758/problems/C/
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item
        
    def __str__(self):
        return f'{self.value} -> {self.next_item}'


def solution(node:Node, idx):
    def get_node_by_index(node:Node, idx):
        while idx:
                node = node.next_item
                idx -= 1
        return node
    if idx == 0:
        node = node.next_item
    else:
        previous_node = get_node_by_index(node, idx-1)
        previous_node.next_item = get_node_by_index(node, idx+1)
    return node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    print(new_head)
test()
    # result is node0 -> node2 -> node3
