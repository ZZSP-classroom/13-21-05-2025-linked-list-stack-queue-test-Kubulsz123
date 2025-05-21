import unittest
from task_scheduler_5 import PriorityQueue

class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = PriorityQueue()
        self.scheduler.add_task("Backup DB", 3)
        self.scheduler.add_task("Send Email", 1)
        self.scheduler.add_task("Update Website", 2)

    def test_priority_order(self):
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Send Email")
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Update Website")
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Backup DB")

    def test_is_empty(self):
        self.assertFalse(self.scheduler.is_empty())
        self.scheduler.process_task()
        self.scheduler.process_task()
        self.scheduler.process_task()
        self.assertTrue(self.scheduler.is_empty())