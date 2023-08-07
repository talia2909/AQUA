import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV,fishtype):
        super().__init__(name, age, x, y, directionH, directionV,fishtype)
        self.width = 8
        self.height = 5


    def get_animal(self):
        x = self.x
        y = self.y
        scalare = [[" " for i in range(x + self.width)] for j in range(y + self.height)]

    #try:
        if self.directionH == 1 :
            for i in range(x, self.width + x):
                if i > 1 + x:
                    scalare[y + 2][i] = "*"
                if i < 6 + x:
                    scalare[y + 0][i] = "*"
                    scalare[y + 4][i] = "*"
                if 4 + x <= i <= 6 + x:
                    scalare[y + 1][i] = "*"
                    scalare[y + 3][i] = "*"
        else:
            for i in range(x, self.width + x):
                if i < self.width + x - 2:
                    scalare[y + 2][i] = "*"
                if i > 2 + x:
                    scalare[y + 0][i] = "*"
                    scalare[y + 4][i] = "*"
                if 1 + x <= i <= 3 + x:
                    scalare[y + 1][i] = "*"
                    scalare[y + 3][i] = "*"
        return scalare
    #except Exception as e:
        #print('board OV', e)


