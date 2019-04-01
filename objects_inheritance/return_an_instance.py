

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

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(3,4)
q = Point(5,12)

mid = p.halfway(q)
print(mid)
print(mid.getX(), mid.getY())