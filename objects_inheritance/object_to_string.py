
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

# the special __str__ method is used to return a string representation of the object
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(4,3)
print(p)
