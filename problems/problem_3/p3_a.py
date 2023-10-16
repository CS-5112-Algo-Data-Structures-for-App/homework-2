'''
Problem 3a
'''

class Node:
    def __init__(self, val:int, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None


    def insert(self, x):
        if self.root is None:
            self.root = Node(x, None)
            return
        
        base = self.root
        while base != None:
            if (base.next == None) or (base.next.val > x):
                new_node = Node(x, base.next)
                base.next = new_node
                return
            base = base.next
        
    def search(self, x):
        base = self.root
        while base != None:
            if base.val == x:
                return base
            base = base.next
        return None

    def delete(self, x):
        base = self.root
        while base != None:
            if base.val == x:
                self.root = base.next
                return
            if base.next == None:
                return
            elif base.next.val == x:
                base.next = base.next.next
                return
            base = base.next

if __name__ == '__main__':
    l = LinkedList()
    l.insert(0)
    l.insert(3)
    l.insert(1)
    l.delete(0)
    print(l.search(0))
    # print(l.root.val)

    