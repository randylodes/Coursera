

class Point:

    # every class uses the initializer method, or constructor
    # it creates the initial attributes for a new instance
    # 'factory default settings'
    # the creation process is called instantiation
    # double underscore can be referred to as 'dunder'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


point1 = Point(5,10)
point2 = Point(1,2)

print(point1.get_x(), point1.get_y())
print(point2.get_x(), point2.get_y())

# 'self' refers to the instance 
# x and y are 'instance variables'




