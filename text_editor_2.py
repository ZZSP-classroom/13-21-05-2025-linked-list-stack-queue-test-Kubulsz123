class Stack:
    def __init__(self):
        self._L = []
    
    def push(self, data):
        return self._L.append(data)
    
    def pop(self):
        if (self.is_empty()):
            return None
        
        return self._L.pop()
    
    def peek(self):
        return self._L[-1]
    
    def is_empty(self):
        if len(self._L) == 0:
            return True
        
        return False
    
    def __str__(self):
        return f"Stack list: {self._L}"
    
undo = Stack()
undo.push("Add Hello World")
undo.push("Delete World")

print("Last operation: ", undo.peek())

undo.pop()

print("Last operation after undo: ", undo.peek())