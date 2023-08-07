import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH,crabtype):
        super().__init__(name, age, x, y, directionH,crabtype)
        self.width = 7
        self.height = 4


    def get_animal(self):
        x = self.x
        y = self.y
        ocypodee=[[" " for i in range(x + self.width)] for j in range(y + self.height)]
    #try:
        for i in range(x, self.width + x):
            if i == x+1 or i== x+5:
                ocypodee[y][i] = "*"
            if x+2 <= i <= x+4:
                ocypodee[y + 1][i] = "*"
            if x <= i <= 6 + x:
                ocypodee[y + 2][i] = "*"
            if i==x or i==6+x:
                ocypodee[y + 3][i] = "*"

    #except Exception as e:
        #print('board OV', e)

        return ocypodee


