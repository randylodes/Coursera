
# This section is on OOP Object Oriented Programing

# have been using OO all along; ex, a string object has various methods:
# string.upper() string.find() string.startswith() etc..
# recall that dir(x) will show available methods for an object
# methods with __underscores__ are internal to Python
# think of compartmentalizing code into logical chunks with 'inner' and 'outer' concerns

# definitions:
# Class - a template
# Method - a function capability built into an object
# Attribute - a piece of data in the object
# Object - a particular instance of a class

# overview of building a class


class PartyAnimal:
    x = 0

    def party(self):  # can be called other than 'self', but self is common convention
        self.x = self.x + 1  # this is like saying "an.x = an.x + 1" in the example
        # can think of 'self' as the object instance
        print("So far", self.x)


an = PartyAnimal()  # the moment of construction

an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))

