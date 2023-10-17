'''
Problem 3b
'''

import random


class Node:
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level
        self.level = level


class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def random_level(self) -> int:
        level = 1
        
        while (random.random() < self.p) and (level < self.max_level):
            level += 1

        
        return level

    def insert(self, x: int) -> None:
        
        update_nodes_lst = [self.sentinel] * self.max_level
        current_node = update_nodes_lst[0]
        
        for i in range(self.max_level - 1, -1, -1):
            while current_node.next[i] is not None:
                if current_node.next[i].val < x:
                    current_node = current_node.next[i]
                
            update_nodes_lst[i] = current_node
            
        current_level_int = self.random_level()
        new_node = Node(x, current_level_int)
        
        for j in range(0,current_level_int):
            new_node.next[j] = update_nodes_lst[j].next[j]
            
            update_nodes_lst[j].next[j] = new_node

        if (not self.root) or (self.root.val > x):
            self.root = new_node



    
    def delete(self, x: int) -> None:
        
        update_nodes_lst = [self.sentinel] * self.max_level
        current_node = update_nodes_lst[0]
        
        for i in range(self.max_level - 1, -1, -1):
            if current_node.next[i] is not None:
                while current_node.next[i].val < x:
                    current_node = current_node.next[i]
                
            update_nodes_lst[i] = current_node

        current_node = current_node.next[0]
        
        if (current_node) and (current_node.val == x):
            for j in range(self.max_level):
                if update_nodes_lst[j].next[j] != current_node:
                    break
                update_nodes_lst[j].next[j] = current_node.next[j]

        if self.root == current_node:
            self.root = current_node.next[0]




    
    def search(self, x: int) -> Node:
        current_node = self.sentinel
        
        for i in range(self.max_level - 1, -1, -1):
            if current_node.next[i] is not None:
                while current_node.next[i].val < x:
                    current_node = current_node.next[i]

        if (current_node.next[0]) is not None:
            if (current_node.next[0].val == x):
                return current_node.next[0]
            else:
                return None
        else:
            return None

