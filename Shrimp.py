import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH,crabtype):
        super().__init__(name, age, x, y, directionH,crabtype)
        self.width = 7
        self.height = 3


    def get_animal(self):
        x = self.x
        y = self.y
        shrimpp=[[" " for i in range(x + self.width)] for j in range(y + self.height)]
        #try:
        if self.directionH == 0:
            for i in range(x, self.width + x):
                if i == x or i == x + 2:
                    shrimpp[y][i] = "*"
                if x + 2 == i or x + 4 == i:
                    shrimpp[y + 2][i] = "*"
                if 1 + x <= i <= 6 + x:
                    shrimpp[y + 1][i] = "*"
        else:
            for i in range(x, self.width + x):
                if i == x + 4 or i == x + 6:
                    shrimpp[y][i] = "*"
                if x + 2 == i or x + 4 == i:
                    shrimpp[y + 2][i] = "*"
                if x <= i <= 5 + x:
                    shrimpp[y + 1][i] = "*"
    #except Exception as e:
        #print('board OV', e)

        return shrimpp

