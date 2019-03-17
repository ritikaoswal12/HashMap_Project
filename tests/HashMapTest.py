import unittest

from hashmap.HashMap import HashMap


class HashMapTest(unittest.TestCase):

    def test_basic_insert(self):
        m = HashMap()
        m.put(1, 1)
        self.assertEqual(1, m.get(1))

    def test_overriding_insert(self):
        m = HashMap()
        m.put(1, 1)
        m.put(1, 2)
        self.assertEqual(2, m.get(1))

    def test_insert_with_collision(self):
        m = HashMap()
        m.put(1, 1)
        m.put(17, 2)
        self.assertEqual(2, m.get(17))

    def test_data_types(self):
        m = HashMap()
        m.put("Ritika", 1)
        m.put(2, "h")
        m.put(1.0, 9.5)
        self.assertEqual(1, m.get("Ritika"))
        self.assertEqual("h", m.get(2))
        self.assertEqual(9.5, m.get(1.0))

    def test_remove(self):
        m = HashMap()
        m.put(1, 1)
        m.put(2, 3)
        m.put(4, 5)
        m.remove(1)
        self.assertEqual(False, m.get(1))

    def test_size(self):
        m = HashMap()
        m.put(1, 1)
        m.put(17, 2)
        self.assertEqual(2, m.map_size())

    def test_rehash(self):
        m = HashMap()
        for i in range(1, 51):
            m.put(i, i)
        self.assertEqual(50, m.map_size())
        self.assertEqual(50, m.get(50))