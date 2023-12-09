import unittest
from SalesItemType import SalesItemType

class SalesItem(object):
    def __init__(self, itemType: SalesItemType, priceIn100s: int, itemCount: int) -> None:
        assert isinstance(itemCount, int), 'itemCount must be integer value'
        assert isinstance(priceIn100s, int), 'priceIn100s must be integer value'
        assert isinstance(itemType, SalesItemType), 'invalid SalesItemType provided'

        self.itemType = itemType
        self.priceIn100s = priceIn100s
        self.itemCount = itemCount

    def increaseItemCount(self, add: int = 1) -> None:
        assert isinstance(add, int), 'add must be integer value'
        self.itemCount = self.itemCount + add

    def totalPriceIn100s(self) -> int:
        return self.itemCount * self.priceIn100s

class TestSalesItem(unittest.TestCase):

    def testSalesItem(self):
        # Show method annotations
        print("SalesItem", SalesItem.__init__.__annotations__)
        print("increaseItemCount", SalesItem.increaseItemCount.__annotations__)
        print("totalPriceIn100s", SalesItem.totalPriceIn100s.__annotations__)

        # Test for invalid parameter type (should be integer count not string)
        with self.assertRaises(AssertionError):
            salesItem = SalesItem(SalesItemType.APPLE,75, "three")
        with self.assertRaises(AssertionError):
            salesItem = SalesItem(SalesItemType.APPLE,"0.75", 3)
        with self.assertRaises(AssertionError):
            salesItem = SalesItem("apple",75, 3)

        salesItem = SalesItem(SalesItemType.APPLE,75, 3)

        self.assertEqual(salesItem.itemType, SalesItemType.APPLE, "SalesItemType is wrong type")
        self.assertEqual(salesItem.priceIn100s, 75, "SalesItemType is wrong price")
        self.assertEqual(salesItem.itemCount, 3, "Number of SalesItemType is wrong")
        salesItem.increaseItemCount()
        self.assertEqual(salesItem.itemCount, 4, "Number of SalesItems is wrong after increment")
        self.assertEqual(salesItem.totalPriceIn100s(), 300, "Total price of SalesItem is wrong after increment")

if __name__ == '__main__':
    unittest.main()
