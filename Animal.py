MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        st = "The animal " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st
    def get_food(self):
        return self.food


    def get_age(self):
        return self.age

    def dec_food(self):
        self.food=self.food-1

    def inc_age(self):
        self.age=self.age+1

    def right(self):
        self.x=self.x-1

    def left(self):
        self.y=self.y-1

    def get_position(self):
        return (self.x,self.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def starvation(self):
        print("The Animal " + str(self.name) + " died at the age of"+ str(self.age) +"Age years Because he ran out of food!")

    def die(self):
        print("The Animal " + str(self.name) + "  died in good health")

    def get_directionH(self):
        return self.directionH


    def set_directionH(self, directionH):
        self.directionH=directionH


    def get_alive(self):
        if self.alive==True:
            return True
        else:
            return False

    def get_size(self):

        pass


    def get_food_amount(self):

        return self.food

    def add_food(self, amount):

        self.food=self.food+amount

    def get_animal(self):
        pass
