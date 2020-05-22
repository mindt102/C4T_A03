
class Queue:
    def __init__(self,capacity,process_rate):
        self.items = []
        self.capacity = capacity
        self.process_rate = process_rate
    def __str__(self):
        return str(self.items)
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        if not self.is_full():
            self.items.insert(0,item)
        else:
            drop_item = item
            return drop_item
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def size(self):
        return len(self.items)
    def is_full(self):
        return (self.size() == self.capacity)

queue = Queue(2)
queue.enqueue(1)
queue.enqueue(2)
print()
