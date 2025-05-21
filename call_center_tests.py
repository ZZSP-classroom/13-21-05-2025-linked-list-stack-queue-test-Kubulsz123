import unittest
from call_center_4 import Queue, Stack, Call

class TestCallCenter(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.stack = Stack()
        self.call1 = Call("123", "09:00")
        self.call2 = Call("456", "17:26")

    def test_enqueue_and_dequeue(self):
        self.queue.enqueue(self.call1)
        self.queue.enqueue(self.call2)
        first = self.queue.dequeue()
        self.assertEqual(first, self.call1)
        self.assertEqual(self.queue.dequeue(), self.call2)

    def test_stack_push_pop(self):
        self.stack.push(self.call1)
        self.stack.push(self.call2)
        last = self.stack.pop()
        self.assertEqual(last, self.call2)
        self.assertEqual(self.stack.pop(), self.call1)

    def test_queue_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(self.call1)
        self.assertFalse(self.queue.is_empty())

    def test_stack_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(self.call1)
        self.assertFalse(self.stack.is_empty())