import unittest
from ItemInventory import ItemInventory
from SalesItem import SalesItem
from SalesItemType import SalesItemType

class ShoppingCart(object):
    def __init__(self, itemInventory: ItemInventory) -> None:
        assert isinstance(itemInventory, ItemInventory), 'invalid ItemInventory provided'
        self.items = []
        self.itemInventory = itemInventory

    def findItem(self, itemType: SalesItemType) -> SalesItem:
        assert isinstance(itemType, SalesItemType), 'invalid SalesItemType provided'
        salesItem = [itemFound for itemFound in self.items if itemType == itemFound.itemType]
        if salesItem.__len__() < 1:
            return None
        else:
            return salesItem[0]

    def addSalesItem(self, itemType: SalesItemType, count: int = 1) -> None:
        assert isinstance(count, int), 'count must be integer value'
        assert (count > 0), 'count must be a positive integer value'
        assert isinstance(itemType, SalesItemType), 'invalid SalesItemType provided'
        newitem = self.findItem(itemType)
        if newitem is None :
            newitem = self.itemInventory.findItem(itemType)
            match newitem:
                case None:
                    print("Item " + itemType.name + " not found in Inventory dropping item from shopping list.")
                case _:
                    self.items.append(newitem)
                    print("Item " + itemType.name + " added to ShoppingCart (1)")
        else:
            print("Item " + itemType.name + " already in ShoppingCart, increment items by " + str(count))
            newitem.itemCount = newitem.itemCount + count

    def itemCount(self) -> int:
        return sum([item.itemCount for item in self.items])

    def totalise(self) -> int:
        return sum([itemFound.itemCount * itemFound.priceIn100s for itemFound in self.items])

    def totalFormattedInPounds(self) -> str:
        pounds = self.totalise()/100
        pence = self.totalise()%100
        return format("%d.%2d" % (pounds, pence))

class TestCart(unittest.TestCase):

    def testCartAdd(self) :
        # Show method annotations
        print("ShoppingCart", ShoppingCart.__init__.__annotations__)
        print("addSalesItem", ShoppingCart.addSalesItem.__annotations__)
        print("findItem", ShoppingCart.findItem.__annotations__)
        print("itemCount", ShoppingCart.itemCount.__annotations__)
        print("totalise", ShoppingCart.totalise.__annotations__)
        print("totalFormattedInPounds", ShoppingCart.totalFormattedInPounds.__annotations__)

        _itemInventory = ItemInventory()
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.ORANGE, 65, 1))
        self.assertEqual(_itemInventory.itemCount(), 2, "ItemInventory has incorrect number of items")
        _itemInventory.addItemToInventory(SalesItem(SalesItemType.APPLE, 45, 1))
        self.assertEqual(_itemInventory.itemCount(), 2, "ItemInventory has incorrect number of items")
        _shoppingCart = ShoppingCart(_itemInventory)
        self.assertEqual(_shoppingCart.itemCount(), 0, "Cart has incorrect number of products")
        # Test for invalid parameter type (should be SalesItemType - APPLE or ORANGE)
        with self.assertRaises(AssertionError):
            _shoppingCart.addSalesItem(3)
        # Test for invalid parameter type (should be integer count not string)
        with self.assertRaises(AssertionError):
            _shoppingCart.addSalesItem(SalesItemType.APPLE, "three")
        _shoppingCart.addSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSalesItem(SalesItemType.APPLE)
        _shoppingCart.addSalesItem(SalesItemType.ORANGE)
        self.assertEqual(_shoppingCart.itemCount(), 4, "Cart has incorrect number of products")
        with self.assertRaises(AssertionError):
            _shoppingCart.addSalesItem(SalesItemType.ORANGE, -2)
        _shoppingCart.addSalesItem(SalesItemType.ORANGE, 2)
        self.assertEqual(_shoppingCart.itemCount(), 6, "Cart has incorrect number of products")
        _shoppingCart.addSalesItem(SalesItemType.BANANA)
        self.assertEqual(_shoppingCart.itemCount(), 6, "Cart has incorrect number of products")
        print("Number of items in cart is", _shoppingCart.itemCount())
        print("Total price is £", _shoppingCart.totalFormattedInPounds())
        self.assertEqual(_shoppingCart.totalise(), 330, "Totalised price not correct")

if __name__ == '__main__':
    unittest.main()


