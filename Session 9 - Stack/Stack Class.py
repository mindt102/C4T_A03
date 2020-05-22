'''
NOTE: 4 kiểu dữ liệu
- Stack LIFO
- Queue FIFO
- Linked list
- Graph
'''

class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    # def __add__(self,s):
    #     return self.items + s.items
    def push(self, item):
        self.items.append(item)
    def remove(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def is_empty(self):
        return (self.items == [])
    def size(self):
        return len(self.items)

class StringProcessor(Stack):
    def reverse(self,string_input):
        for c in string_input:
            self.push(c)
        result = ""
        while not self.is_empty():    
            result += self.remove()
        return result
    def decimal_to_binary(self,number):
        while number != 0:
            self.push(number % 2)
            number = number // 2
        result = 0
        while not self.is_empty():
            result = result*10 + self.remove()
        return result
    def is_balanced(self,expression_string):
        open_bracket  = ["(","[","{"]
        close_bracket = [")","]","}"]
        for c in expression_string:
            if c in open_bracket:
                self.push(c)
            if not self.is_empty() and c in close_bracket:
                current_bracket_index = close_bracket.index(c)
                if open_bracket[current_bracket_index] != self.remove():
                    return False
        if self.is_empty():
            return True
        else:
            return False
stack = StringProcessor()
print(stack.is_balanced('(([][)'))
