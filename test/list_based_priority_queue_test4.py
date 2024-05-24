import unittest
from list_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_insert_empty_queue(self):
        self.queue.insert(1, 10)
        self.assertIsNotNone(self.queue.head)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.head.priority, 10)

    def test_insert_higher_priority(self):
        self.queue.insert(1, 10)
        self.queue.insert(2, 20)
        self.assertEqual(self.queue.head.value, 2)
        self.assertEqual(self.queue.head.priority, 20)
        self.assertEqual(self.queue.head.next.value, 1)
        self.assertEqual(self.queue.head.next.priority, 10)

    def test_insert_lower_priority(self):
        self.queue.insert(2, 20)
        self.queue.insert(1, 10)
        self.assertEqual(self.queue.head.value, 2)
        self.assertEqual(self.queue.head.priority, 20)
        self.assertEqual(self.queue.head.next.value, 1)
        self.assertEqual(self.queue.head.next.priority, 10)

    def test_remove_highest_priority(self):
        self.queue.insert(1, 10)
        self.queue.insert(2, 20)
        self.queue.insert(3, 30)
        self.assertEqual(self.queue.remove_highest_priority(), 3)
        self.assertEqual(self.queue.head.value, 2)
        self.assertEqual(self.queue.head.priority, 20)

if __name__ == '__main__':
    unittest.main()