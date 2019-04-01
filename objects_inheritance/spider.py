class Animal:

    def __init__(self, num1, num2):
        self.arms = int(num1)
        self.legs = int(num2)

    def limbs(self):
        return self.arms + self.legs


spider = Animal(4, 4)
spidlimbs = spider.limbs()
print(spidlimbs)

