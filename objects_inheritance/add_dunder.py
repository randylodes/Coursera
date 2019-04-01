

# this is an example of 'overriding' some of the special dunder methods to produce the results we desire for this object

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    # the special __add__ method is used to allow mathematical addition of point objects
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)

    # could also use __sub__ for subtraction
    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)

p1 = Point(-5,10)
p2 = Point(15,20)
print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)
