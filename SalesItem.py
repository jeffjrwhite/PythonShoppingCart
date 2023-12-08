import unittest
from SalesItemType import SalesItemType

class SalesItem(object):
    def __init__(self, itemType, priceIn100s, itemCount):
        self.itemType = itemType
        self.priceIn100s = priceIn100s
        self.itemCount = itemCount

    def incrementItemCount(self):
        self.itemCount = self.itemCount + 1

    def increaseItemCount(self, add):
        self.itemCount = self.itemCount + add

    def totalPriceIn100s(self):
        return self.itemCount * self.priceIn100s

class TestSalesItem(unittest.TestCase):

    def testSalesItem(self):
        salesItem = SalesItem(SalesItemType.APPLE,0.75, 3)

        self.assertEqual(salesItem.itemType, SalesItemType.APPLE, "SalesItemType is wrong type")
        self.assertEqual(salesItem.priceIn100s, 0.75, "SalesItemType is wrong price")
        self.assertEqual(salesItem.itemCount, 3, "Number of SalesItemType is wrong")
        salesItem.incrementItemCount()
        self.assertEqual(salesItem.itemCount, 4, "Number of SalesItems is wrong after increment")
        self.assertEqual(salesItem.totalPriceIn100s(), 3, "Total price of SalesItem is wrong after increment")

if __name__ == '__main__':
    unittest.main()
