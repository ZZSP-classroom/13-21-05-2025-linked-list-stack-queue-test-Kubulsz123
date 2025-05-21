import unittest
from text_editor_2 import Stack

class TestHospital(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.operation1 = "Add Hello World"
        self.operation2 = "Delete World"
    
    def test_push_peek(self):
        self.stack.push(self.operation1)
        self.assertEqual(self.stack.peek(), self.operation1)

        self.stack.push(self.operation2)
        self.assertEqual(self.stack.peek(), self.operation2)
    
    def test_dequeue(self):
        self.stack.push(self.operation1)
        self.stack.push(self.operation2)

        removed = self.stack.pop()

        self.assertEqual(removed, self.operation2)
        self.assertEqual(self.stack.peek(), self.operation1)
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(self.operation1)
        self.assertFalse(self.stack.is_empty())
