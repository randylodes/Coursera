CURRENT_YEAR = 2019


class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    def getAge(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())


alice = Person('Alice Smith', 1990)
print(alice)


# Student will inherit from the Person class
# put the parent class in the parens


class Student(Person):
    def __init__(self, name, year_born):
        # this is using the __init__ method from Person class
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1

# the Student class has inherited the Person methods (getAge, __str__, etc)

alice = Student('Alice Smith', 1990)
alice.study()
print(alice)
print(alice.knowledge)
print(alice.getAge())