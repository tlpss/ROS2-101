import unittest

from talker_listener_python.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def test_sequence(self):
        fib = Fibonacci()

        fib_list = [fib(), fib(), fib(), fib()]
        desired_list = [1, 2, 3, 5]
        self.assertListEqual(fib_list, desired_list)
