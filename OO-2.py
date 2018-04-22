# continuing with OO concepts

# Object Lifecycle:
# objects are created, used, discarded
# methods exist for creation (constructor) and destruction (destructor)
# constructors are commonly used more than destructors


class PartyAnimal:
    x = 0

    def __init__(self):   # the constructor is optional; typically used to set up variables
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):  # the destructor is rarely used
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)


# Similar approach, adding 'name' and working with multiple instances
class PartyAnimal2:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


s = PartyAnimal2('Sally')
s.party()

j = PartyAnimal2('Jim')
j.party()
s.party()
