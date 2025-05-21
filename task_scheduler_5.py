class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.next = None

    def __str__(self):
        return f"Task({self.task_name}, priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.head = None

    def add_task(self, task_name, priority):
        new_task = Task(task_name, priority)
        if self.head is None or priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def process_task(self):
        if self.head is None:
            return None
        task = self.head
        self.head = self.head.next
        return task

    def is_empty(self):
        return self.head is None

    def __str__(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(repr(current))
            current = current.next
        return " -> ".join(tasks)


pq = PriorityQueue()
pq.add_task("Backup DB", 3)
pq.add_task("Send Email", 1)
pq.add_task("Update Website", 2)

print("Task queue:", pq)
print("Processing:", pq.process_task())
print("Remaining:", pq)