class Queue:
    def __init__(self,):
        self._L = []
    
    def enqueue(self, data):
        return self._L.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self._L.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self._L[0]
    
    def is_empty(self):
        if len(self._L) == 0:
            return True
        
        return False
    
    def __str__(self):
        return f"Queue list: {self._L}"
    

class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time
    
    def __str__(self):
        return f"Patient: {self.name} -> {self.appointment_time}"
    

queue = Queue()
queue.enqueue(Patient("Jakub", "12:30"))
queue.enqueue(Patient("Adam", "9:47"))

print("Next: ", queue.peek())

queue.dequeue()

print("Next: ", queue.peek())