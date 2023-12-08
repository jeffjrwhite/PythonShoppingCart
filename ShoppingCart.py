import unittest
from ItemInventory import ItemInventory
from SalesItem import SalesItem
from SalesItemType import SalesItemType

class ShoppingCart(object):
    def __init__(self, itemInventory):
        self.items = []
        self.itemInventory = itemInventory

    def findItem(self, itemType):
        salesItem = [itemFound for itemFound in self.items if itemType == itemFound.itemType]
        if salesItem.__len__() < 1:
            return None
        else:
            return salesItem[0]

    def addSingleSalesItem(self, itemType):
        self.addSalesItem(itemType, 1)

    def addSalesItem(self, itemType, count):
        newitem = self.findItem(itemType)
        if newitem is None :
            newitem = self.itemInventory.findItem(itemType)
            match newitem:
                case None:
                    print("Item " + itemType.name + " not found in Inventory dropping item from shopping list.")
                case _:
                    self.items.append(newitem)
                    print("Item " + itemType.name + " added to ShoppingCart")
        else:
            print("Item " + itemType.name + " already in ShoppingCart, increment items by count")
            newitem.itemCount = newitem.itemCount + count

    def itemCount(self):
        return sum([item.itemCount for item in self.items])

class TestCart(unittest.TestCase):

    def testCartAdd(self):

        _itemInventory = ItemInventory()
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.ORANGE, 65, 1))
        self.assertEqual(_itemInventory.itemCount(), 2, "ItemInventory has incorrect number of items")
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        self.assertEqual(_itemInventory.itemCount(), 2, "ItemInventory has incorrect number of items")
        _shoppingCart = ShoppingCart(_itemInventory)
        self.assertEqual(_shoppingCart.itemCount(), 0, "Cart has incorrect number of products")
        _shoppingCart.addSingleSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSingleSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSingleSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSingleSalesItem(SalesItemType.ORANGE)
        self.assertEqual(_shoppingCart.itemCount(), 4, "Cart has incorrect number of products")
        _shoppingCart.addSalesItem(SalesItemType.ORANGE, 2)
        self.assertEqual(_shoppingCart.itemCount(), 6, "Cart has incorrect number of products")
        _shoppingCart.addSingleSalesItem(SalesItemType.BANANA)

if __name__ == '__main__':
    unittest.main()


