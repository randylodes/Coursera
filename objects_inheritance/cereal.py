
class Cereal:

    def __init__(self, s1, s2, i):
        self.name = s1
        self.brand = s2
        self.fiber = i

    def __str__(self):
        return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)


c1 = Cereal('Corn Flakes', "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)

