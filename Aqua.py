import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120
y_bottom_scalar=10
y_bottom_molly=8


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []
        self.crabs = []


    def build_tank(self):
        x=self.aqua_width
        y=self.aqua_height
        self.board=[[" " for i in range(x)] for j in range(y)]
        for i in range(y):
            self.board[i][0] = "|"
            self.board[i][x - 1] = "|"
        for i in range(1, x - 1):
            self.board[2][i] = '~'
            self.board[y - 1][i] = "-"
        self.board[y - 1][x - 1] = "/"
        self.board[y - 1][0] = chr(92)
        return self.board


    def print_board(self):
        y=self.aqua_height
        for i in range(y):
            print(' '.join([str(elem) for elem in self.board[i]]))



    def get_board(self):
        return self.board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):

        """
        Returns True if the next step of the crab is a collision
        """
        counter=0
        for i in range(len(self.crabs)):
            for j in range(i+1,len(self.crabs)):
                if (self.crabs[i].x == 1 and self.crabs[i].directionH == 0):
                    counter=1
                    self.crabs[i].directionH = 1
                if (self.crabs[i].x == self.aqua_width - 8 and self.crabs[i].directionH == 1):
                    counter=1
                    self.crabs[i].directionH = 0
                if (self.crabs[j].x == 1 and self.crabs[j].directionH == 0):
                    counter=1
                    self.crabs[j].directionH = 1
                if (self.crabs[j].x == self.aqua_width - 8 and self.crabs[j].directionH == 1):
                    counter=1
                    self.crabs[j].directionH = 0
                if (self.crabs[i].x > self.crabs[j].x and self.crabs[i].directionH == 0 and self.crabs[j].directionH == 1 and self.crabs[i].x - self.crabs[j].x <= 8):
                    counter=1
                    self.crabs[i].directionH = 1
                    self.crabs[j].directionH = 0
                if (self.crabs[i].x < self.crabs[j].x and self.crabs[i].directionH == 1 and self.crabs[j].directionH == 0 and self.crabs[j].x - self.crabs[i].x <= 8):
                    counter=1
                    self.crabs[i].directionH = 0
                    self.crabs[j].directionH = 1


        if counter== 1:
            return True
        else:
            return False

        """
        Returns True if the next step of the crab is a collision
        """


    def print_animal_on_board(self, animal: Animal):

        arr=animal.get_animal()
        for i in range(len(arr)):
            for j in range(animal.x+animal.width):
                if arr[i][j]!= " " :
                    self.board[i][j] = arr[i][j]


    def delete_animal_from_board(self, animal: Animal):
        if animal.age >= 120 or animal.food == 0:
            if isinstance(animal, Fish.Fish):
                if animal.age >= 120:
                    animal.die()
                    animal.alive=False
                if animal.food <= 0:
                    animal.starvation()
                    animal.alive=False

            if isinstance(animal, Crab.Crab):
                if animal.age >= 120:
                    animal.die()
                    animal.alive=False
                if animal.food <= 0:
                    animal.starvation()
                    animal.alive=False
                    return False
        else:
            return animal

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """

        new_fish = Fish.Fish(name, age, x, y, directionH, directionV,fishtype)
        x=new_fish.x
        y=new_fish.y
        fishtype=new_fish.fishtype
        if fishtype == 'sc':
            while (y > self.aqua_height - y_bottom_scalar):
                y =self.up(y)
            while (2 >= y):
                y = self.down(y)
            while (self.aqua_width - 9 < x):
                x = self.left(x)
            while (x < 0):
                x = self.right(x)
            if self.check_if_free(x,y):
                new_fish.x=x
                new_fish.y=y
                sc = Scalar.Scalar(name, age, x, y, directionH, directionV,fishtype)
                self.anim.append(new_fish)
                self.print_animal_on_board(sc)
                return True
            else:
                print("The place is not available! Please try again later")
                return False

        if fishtype == 'mo':
            while (y > self.aqua_height - y_bottom_molly):
                y = self.up(y)
            while (2 >= y):
                y = self.down(y)
            while (self.aqua_width - 9 < x):
                x = self.left(x)
            while (x < 0):
                x = self.right(x)
            if self.check_if_free(x, y):
                new_fish.x=x
                new_fish.y=y
                mo = Moly.Moly(name, age, x, y, directionH, directionV,fishtype)
                self.anim.append(new_fish)
                self.print_animal_on_board(mo)

                return True

            else:
                print("The place is not available! Please try again later")
                return False


    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        new_crab = Crab.Crab(name, age, x, y, directionH,crabtype)
        x=new_crab.x
        if crabtype == 'sh':
            while (self.aqua_width - 8 < x):
                x = self.left(x)
            while (x < 0):
                x = self.right(x)
            if self.check_if_free(x,y=-1):
                new_crab.x=x
                s1 = Shrimp.Shrimp(name, age, x,self.aqua_height-4 , directionH,crabtype)
                self.anim.append(new_crab)
                self.print_animal_on_board(s1)

                return True
            else:
                print("The place is not available! Please try again later")
                return False

        if crabtype == 'oc':
            while (self.aqua_width - 8 < x):
                x = self.left(x)
            while (x < 0):
                x = self.right(x)
            if self.check_if_free(x,y=-1):
                new_crab.x=x
                o1 = Ocypode.Ocypode(name, age, x, self.aqua_height-5, directionH,crabtype)
                self.anim.append(new_crab)
                self.print_animal_on_board(o1)

                return True
            else:
                print("The place is not available! Please try again later")
                return False




    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        if self.turn > 0:
            return True


        else:
            counter1 = 0
            if y==-1:
                y=self.aqua_height-6
                for i in range(y, y+5):
                    for j in range(x, x + 7):
                        if (self.board[i][j] == ' '):
                            counter1 = counter1 + 1

                if (counter1 == 35):
                    return True

            else :
                for i in range(y, y + 8):
                    for j in range(x, x + 8):
                        if (self.board[i][j] == ' '):
                            counter1 = counter1 + 1

                if (counter1 == 64):
                    return True

    def left(self, a):
        a.x = a.x-1
        return a.x

    def right(self, a):
        a.x=a.x+1
        return a.x
    def up(self, a):
        a.y=a.y-1
        return a.y

    def down(self, a):
        a.y=a.y+1
        return a.y

    def next_turn(self):
        self.turn += 1

        """
        Managing a single step
        """

        length=len(self.anim)
        self.board = self.build_tank()
        for i in range(len(self.anim)):
            if (self.turn) % 100 == 0:
                self.anim[i].age +=1
            if isinstance (self.anim[i],Fish.Fish) :
                name=self.anim[i].name
                age=self.anim[i].age
                x=self.anim[i].x
                y=self.anim[i].y
                diH=self.anim[i].directionH
                diV=self.anim[i].directionV
                fishtype=self.anim[i].fishtype
                food=self.anim[i].food
                self.anim[i]=" "
                if fishtype=='sc':
                    y_bottom=y_bottom_scalar
                if fishtype=='mo':
                    y_bottom=y_bottom_molly
                if diH==0 and diV==0:
                    if x==1 and  y!=self.aqua_height-y_bottom :
                        fish = self.add_fish(name, age, x + 1, y + 1, 1, diV, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if y==self.aqua_height-y_bottom and x!=1 :
                        fish = self.add_fish(name, age, x - 1, y - 1, diH, 1, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if  x==1 and  y==self.aqua_height-y_bottom :
                        fish = self.add_fish(name, age, x + 1, y - 1, 1, 1, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    elif x!=1 and  y!=self.aqua_height-y_bottom:
                        fish = self.add_fish(name, age, x-1, y+1, diH, diV,fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else :
                            self.anim[-1].food=food
                if diH==1 and diV==0 :
                    if x==self.aqua_width-9 and  y!=self.aqua_height-y_bottom :
                        fish = self.add_fish(name, age, x - 1, y + 1, 0, diV, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if y==self.aqua_height-y_bottom and x!=self.aqua_width-2 :
                        fish = self.add_fish(name, age, x + 1, y - 1, diH, 1, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if  x==self.aqua_width-9 and  y==self.aqua_height-y_bottom :
                        fish = self.add_fish(name, age, x - 1, y - 1, 0, 1, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    elif x!=self.aqua_width-9 and  y!=self.aqua_height-y_bottom:
                        fish = self.add_fish(name, age, x+1, y+1, diH, diV,fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                if diH == 0 and diV == 1:
                    if x==1 and  y!=3 :
                        fish = self.add_fish(name, age, x + 1, y - 1, 1, diV, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if y==3 and x!=1 :
                        fish = self.add_fish(name, age, x - 1, y + 1, diH, 0, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if  x==1 and  y==3 :
                        fish = self.add_fish(name, age, x + 1, y + 1, 1, 0, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    elif x!=1 and  y!=3 :
                        fish = self.add_fish(name, age, x-1, y-1, diH, diV,fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                if diH == 1 and diV == 1:
                    if x == self.aqua_width-9 and y != 3:
                        fish = self.add_fish(name, age, x - 1, y - 1, 0, diV, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if y == 3 and x != self.aqua_width-2:
                        fish = self.add_fish(name, age, x + 1, y + 1, diH, 0, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    if x == self.aqua_width-9 and y == 3:
                        fish = self.add_fish(name, age, x - 1, y + 1, 0, 0, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food
                    elif x!=self.aqua_width-9 and y!=3:
                        fish = self.add_fish(name, age, x + 1, y - 1, diH, diV, fishtype)
                        if (self.turn) % 10 == 0:
                            self.anim[-1].food = food - 1
                        else:
                            self.anim[-1].food = food

            if isinstance(self.anim[i],Crab.Crab) :
                food = self.anim[i].food
                self.crabs.append(self.anim[i])
                self.anim[i] = " "


        if self.is_collision(self.crabs) :
            for i in range(len(self.crabs)):
                if self.crabs[i].directionH==1 :
                    crab = self.add_crab(self.crabs[i].name, self.crabs[i].age, self.crabs[i].x+1, -1, self.crabs[i].directionH,self.crabs[i].crabtype)
                    if (self.turn) % 10 == 0:
                        self.anim[-1].food = food - 1
                    else:
                        self.anim[-1].food = food
                elif self.crabs[i].directionH==0 :
                    crab = self.add_crab(self.crabs[i].name, self.crabs[i].age, self.crabs[i].x-1 , -1, self.crabs[i].directionH, self.crabs[i].crabtype)
                    if (self.turn) % 10 == 0:
                        self.anim[-1].food = food - 1
                    else:
                        self.anim[-1].food = food
        elif  not self.is_collision(self.crabs) :
            for i in range(len(self.crabs)):
                if self.crabs[i].directionH==1 :
                    crab = self.add_crab(self.crabs[i].name, self.crabs[i].age, self.crabs[i].x+1, -1, self.crabs[i].directionH,self.crabs[i].crabtype)
                    if (self.turn) % 10 == 0:
                        self.anim[-1].food = food - 1
                    else:
                        self.anim[-1].food = food
                elif self.crabs[i].directionH==0 :
                    crab = self.add_crab(self.crabs[i].name, self.crabs[i].age, self.crabs[i].x-1 , -1, self.crabs[i].directionH, self.crabs[i].crabtype)
                    if (self.turn) % 10 == 0:
                        self.anim[-1].food = food - 1
                    else:
                        self.anim[-1].food = food
        self.crabs=[]


        self.anim=self.anim[length:]
        update_anim=[]
        for i in range(len(self.anim)):
            animal_in=self.delete_animal_from_board(self.anim[i])
            if animal_in :
                update_anim.append(animal_in)

        self.anim=update_anim









    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for i in range(len(self.anim)):
            if (type(self.anim[i])) == Fish.Fish:
                print(Fish.Fish.__str__(self.anim[i]))
            if type(self.anim[i])==Crab.Crab:
                print(Crab.Crab.__str__(self.anim[i]))


    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for i in range (len(self.anim)):
            self.anim[i].food = self.anim[i].food +10

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:

        """
        Managing several steps
        """
        n_step=int(input("How many steps do you want to take?"))
        if n_step==0:
            self.print_board()
        else:
            for i in range(n_step):
                self.next_turn()
            self.print_board()
