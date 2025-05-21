class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

    def __str__(self):
        return f"Call({self.caller_id}, {self.time_received})"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, call):
        self.items.append(call)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Queue({self.items})"


class Stack:
    def __init__(self):
        self.items = []

    def push(self, call):
        self.items.append(call)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Stack({self.items})"

incoming_calls = Queue()
processing_calls = Stack()

incoming_calls.enqueue(Call("123", "09:00"))
incoming_calls.enqueue(Call("456", "17:26"))

print("Incoming:", incoming_calls)

call = incoming_calls.dequeue()
processing_calls.push(call)

print("Processing:", processing_calls)