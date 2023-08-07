import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH,crabtype):
        super().__init__(name, age, x, y, directionH)
        self.width = MAX_CRAB_WIDTH
        self.height = MAX_CRAB_HEIGHT
        self.crabtype=crabtype

    def __str__(self):
        st = "The Crab " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st


    def starvation(self):
        print("The crab " + str(self.name) + " died at the age of"+ str(self.age) +"Age years Because he ran out of food!")

    def die(self):
        print("The crab "+ str(self.name) + " died in good health")

    def up(self):
        self.x = self.x + 1

    def down(self):
        self.y = self.y - 1
