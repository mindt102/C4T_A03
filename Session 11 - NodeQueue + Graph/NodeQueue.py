class Node:
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next  = next
    def __str__(self):
        return '{}'.format(self.cargo)

class NodeQueue:
    def __init__ (self,capacity):
        self.length = 0
        self.head  = None
        self.capacity = capacity
    def is_empty(self):
        return self.length == 0
    def is_full(self):
        return self.length == self.capacity
    def enqueue(self,cargo):
        if not self.is_full():
            if self.is_empty():
                self.head = Node(cargo)
            else:
                last_node = self.head
                while last_node.next != None:
                    last_node = last_node.next
                last_node.next = Node(cargo)
            self.length += 1
        else:
            return cargo
    def dequeue(self):
        if not self.is_empty():
            first_node = self.head
            self.head = self.head.next
            self.length -= 1
            return first_node.cargo
        else:
            return None