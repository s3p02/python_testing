import unittest
import sys
class My_unittest(unittest.TestCase):
    def test(self):
        self.assertEqual(add_1(2),3)

def add_1(add_val):
    """
    This function returns a value by ading 1 to it
    Arguments:
    add_val --> input value to function
    """
    #Begin add_1()
    return add_val + 1
    #End add_1()

def main():
    """
    Main Function
    Arguments:
    argv[0]: Python Script
    """
    #Begin main()
    script=sys.argv[0]
    #End main()

if __name__ == '__main__':
    unittest.main()
