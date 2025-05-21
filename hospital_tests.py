import unittest
from hospital_1 import Queue, Patient

class TestHospital(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.patient1 = Patient("Jakub", "12:30")
        self.patient2 = Patient("Adam", "9:47")
    
    def test_enqueue_peek(self):
        self.queue.enqueue(self.patient1)
        self.assertEqual(self.queue.peek(), self.patient1)

        self.queue.enqueue(self.patient2)
        self.assertEqual(self.queue.peek(), self.patient1)
    
    def test_dequeue(self):
        self.queue.enqueue(self.patient1)
        self.queue.enqueue(self.patient2)

        removed = self.queue.dequeue()

        self.assertEqual(removed, self.patient1)
        self.assertEqual(self.queue.peek(), self.patient2)
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(self.patient1)
        self.assertFalse(self.queue.is_empty())
