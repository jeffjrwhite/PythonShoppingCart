import unittest
from SalesItem import SalesItem
from SalesItemType import SalesItemType


class ItemInventory(object):
    def __init__(self):
        self.items = []

    def addItemToInventory(self, newitem: SalesItem):
        assert isinstance(newitem, SalesItem), 'invalid SalesItem provided'
        if newitem.itemType in [items.itemType for items in self.items]:
            print("Item " + newitem.itemType.name + " already in Inventory")
        else:
            self.items.append(newitem)
            print("Item " + newitem.itemType.name + " added to Inventory")

    def findItem(self, itemType: SalesItemType) -> SalesItem:
        assert isinstance(itemType, SalesItemType), 'invalid SalesItemType provided'
        inventoryItem = [itemFound for itemFound in self.items if itemType == itemFound.itemType]
        if inventoryItem.__len__() < 1:
            return None
        else:
            return inventoryItem[0]

    def itemCount(self) -> int:
        return self.items.__len__()

class TestItemInventory(unittest.TestCase):

    def testItemInventory(self):
        itemInventory = ItemInventory()
        # Test for invalid parameter type (should be SalesItem not string)
        with self.assertRaises(AssertionError):
            itemInventory.addItemToInventory("apple")
        itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        itemInventory.addItemToInventory(SalesItem(SalesItemType.ORANGE, 65, 1))
        self.assertEqual(itemInventory.items.__len__(), 2, "ItemInventory has incorrect number of items")
        itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        self.assertEqual(itemInventory.items.__len__(), 2, "ItemInventory has incorrect number of items")
        print([itemFound for itemFound in itemInventory.items])
        # Test for invalid parameter type (should be SalesItemType not string)
        with self.assertRaises(AssertionError):
            itemInventory.findItem("apple")
        orange = itemInventory.findItem(SalesItemType.ORANGE)
        print("Orange found ", orange.itemType)
        self.assertEqual(orange.itemType, SalesItemType.ORANGE, "ORANGE not found in Inventory")

if __name__ == '__main__':
    unittest.main()


