import unittest
from enum import Enum

class SalesItemType(Enum) :
        APPLE = 1
        ORANGE = 2
        BANANA = 3

class TestSalesItemType(unittest.TestCase):

    def testSalesItemType(self):
        print(SalesItemType.__annotations__)
        apple = SalesItemType.APPLE
        orange = SalesItemType.ORANGE
        self.assertNotEqual(apple, orange, "ENUMs are the same")
        print(apple)

if __name__ == '__main__':
    unittest.main()
