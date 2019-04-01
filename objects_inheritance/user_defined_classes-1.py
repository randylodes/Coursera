

# In python every value is actually an object

# convention is to start with capital letter and use camel-case
# parens are optional

class Point():

    # a method is simply a function that lives inside a class
    # one difference is that there is always at least one argument (self)
    def getX(self):
        return self.x


# creating instances of 'Point'
point1 = Point()
point2 = Point()

# these ate class objects
print(point1)
print(point2)

# these are different objects
print(point1 == point2)

# create instance variables
point1.x = 5
point2.x = 10

print(point1.x)
print(point2.x)

print(point1.getX())
print(point2.getX())


