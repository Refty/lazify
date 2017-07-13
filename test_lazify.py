import unittest

from lazify import LazyProxy, lazify


class LazyProxyTestCase(unittest.TestCase):

    def test_proxy_caches_result_of_function_call(self):
        self.counter = 0

        def add_one():
            self.counter += 1
            return self.counter
        proxy = LazyProxy(add_one)
        self.assertEqual(1, proxy.value)
        self.assertEqual(1, proxy.value)

    def test_can_disable_proxy_cache(self):
        self.counter = 0

        def add_one():
            self.counter += 1
            return self.counter
        proxy = LazyProxy(add_one, enable_cache=False)
        self.assertEqual(1, proxy.value)
        self.assertEqual(2, proxy.value)

    def test_can_copy_proxy(self):
        from copy import copy

        numbers = [1, 2]

        def first(xs):
            return xs[0]

        proxy = LazyProxy(first, numbers)
        proxy_copy = copy(proxy)

        numbers.pop(0)
        self.assertEqual(2, proxy.value)
        self.assertEqual(2, proxy_copy.value)

    def test_can_deepcopy_proxy(self):
        from copy import deepcopy
        numbers = [1, 2]

        def first(xs):
            return xs[0]

        proxy = LazyProxy(first, numbers)
        proxy_deepcopy = deepcopy(proxy)

        numbers.pop(0)
        self.assertEqual(2, proxy.value)
        self.assertEqual(1, proxy_deepcopy.value)


class LazyTestCase(unittest.TestCase):

    def test_cache(self):
        numbers = [1, 2, 3]

        @lazify
        def first(xs):
            return xs.pop(0)

        proxy = first(numbers)
        self.assertEqual(1, proxy.value)
        self.assertEqual(1, proxy.value)

        proxy = first(numbers, enable_cache=False)
        self.assertEqual(2, proxy.value)
        self.assertEqual(3, proxy.value)
