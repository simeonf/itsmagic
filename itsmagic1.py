"""Simple Python objects & methods are pretty straightforwards.

But many of the complex behaviors of built in types can be implemented
by adding the right __method__. See
https://docs.python.org/2/reference/datamodel.html#special-method-names
for a complete list.

Fill in the implementation below to make the tests pass.

Classes should have an informal and a formal string representation. Do
you know about repr?

>>> a = Point2D(4, 5)
>>> print(a)
(4, 5)
>>> a
<Point {x: 4, y: 5}>

You might also add support for common operators like + and -, < and >, and ==.

>>> a = Point2D(4, 5)
>>> b = Point2D(1, 2)
>>> a < b  # For a vector use distance from origin point.
False
>>> a > b
True
>>> c = a + b
>>> c
<Point {x: 5, y: 7}>
>>> c - b == a
True

Extra Credit! Investigate and use functools.total_ordering

"""
