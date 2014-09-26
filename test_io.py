import os
import unittest
from PhotoShop import Customer, PhotoQueue, reader


class IOTest(unittest.TestCase):

    data = 'data/Photos.csv'

    def test_data(self):
        self.assertTrue(os.path.isfile(self.data))

    def test_customer(self):
        self.assertEqual(Customer.__base__, tuple)
        self.assertEqual(Customer._fields, ('name', 'photos'))

    def test_queue(self):
        queue = PhotoQueue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(Customer('Sang Han', 42))
        self.assertEqual(len(queue), 1)
        self.assertIsInstance(queue.dequeue(), Customer)

    def test_reader(self):
        queue = reader(self.data)
        self.assertIsInstance(queue, PhotoQueue)
        self.assertFalse(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
