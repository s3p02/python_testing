import unittest

def add_1(add_val):
    return add_val + 1

class My_unittest(unittest.TestCase):
    def test(self):
        self.assertEqual(add_1(2),3)

if __name__ == '__main__':
    unittest.main()
