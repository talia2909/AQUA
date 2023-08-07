import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV,fishtype):
        super().__init__(name, age, x, y, directionH, directionV,fishtype)
        self.width = 8
        self.height = 3




    def get_animal(self):
        x = self.x
        y = self.y
        molyy=[[" " for i in range(x + self.width)] for j in range(y + self.height)]
        #try:
        if self.directionH == 0:
            for i in range(x, self.width + x):
                if x <= i <= x + 7:
                    molyy[y + 1][i] = "*"
                if i == 7 + x:
                    molyy[y + 0][i] = "*"
                    molyy[y + 1][i] = "*"
                    molyy[y + 2][i] = "*"
                if x < i <= 4 + x:
                    molyy[y][i] = "*"
                    molyy[y + 1][i] = "*"
                    molyy[y + 2][i] = "*"
        else:
            for i in range(x, self.width + x):
                if x <= i <= x + 7:
                    molyy[y + 1][i] = "*"
                if i == x:
                    molyy[y + 0][i] = "*"
                    molyy[y + 1][i] = "*"
                    molyy[y + 2][i] = "*"
                if x + 2 < i <= 6 + x:
                    molyy[y][i] = "*"
                    molyy[y + 1][i] = "*"
                    molyy[y + 2][i] = "*"
    #except Exception as e:
        #print('board OV', e)

        return molyy



