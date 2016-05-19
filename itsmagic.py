"""
Classes are pretty straighforwards in Python. All you need to understand is

* Class naming conventions
* inheritance (you don't actually need to understand this!)
* the constructor
* "self"
* methods

For example a simple class with one attribute could be created with:

>>> class Sample(object):
...     def __init__(self, value):
...         self.value = value
>>> o1 = Sample(5)
>>> o2 = Sample(6)
>>> o2.value
6
>>> o1.value
5

Let's make some simple Python classes. The only "magic" method you need is __init__.

Create a Point2D class with x and y attributes.

>>> a = Point2D(4, 5)
>>> a.x
4
>>> a.y
5

Use Pythagorean's theorem to measure the distance between points.

>>> a = Point2D(4, 5)
>>> origin = Point2D(0, 0)
>>> "%.2f" % a.distance(origin)
'6.40'


Create a Box class defined by two points - the top_left and bottom_right.

>>> box = Box(Point2D(0, 5), Point2D(5, 1))
>>> box.top_left.x
0
>>> box.top_left.y
5
>>> box.bottom_right.x
5
>>> box.bottom_right.y
1

You shouldn't be able to create impossible boxes!

>>> Box(Point2D(5,0), Point2D(0,0))
Traceback (most recent call last):
...
ValueError: top_left must be left and above bottom_right


"""

# Add your code here to make the tests pass.
