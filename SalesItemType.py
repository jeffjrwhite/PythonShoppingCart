import unittest
from enum import Enum

class SalesItemType(Enum):
        APPLE = 1
        ORANGE = 2
        BANANA = 3

class TestSalesItemType(unittest.TestCase):

    def testSalesItemType(self):
        apple = SalesItemType.APPLE
        orange = SalesItemType.ORANGE
        self.assertNotEqual(apple, orange, "ENUMs are the same")

if __name__ == '__main__':
    unittest.main()
