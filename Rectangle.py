import unittest

# Our code to be tested
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def testRectangle(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")

    def testListManipulation(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        odd = x[::2]
        even = x[1::2]
        #print(odd)
        #print(even)
        #print(x[3:4])
        #print [9,7,5,3,1]? How about [7,5,3]
        #print(x[-2::-2])
        #print(x[-4:1:-2])
        self.assertEqual(x[-2::-2], [9,7,5,3,1], 'List test 1 failed')
        self.assertEqual(x[-4:1:-2], [7,5,3], 'List test 2 failed')

# run the test
if __name__ == '__main__':
    unittest.main()