
# Object Inheritance
# multiple templates that are related
# reuse an existing class and add some new elements
# the 'child' class 'inherits' capabilities from the 'parent' class
# can also be called a subclass - a specialized version a particular class
# just another form of 'store and reuse'


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal) :
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)


s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()

# class 'FootballFan' is just extending class 'PartyAnimal'
# by adding code for 'points' and 'touchdown'







