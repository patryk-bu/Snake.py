import random
import keyboard


# class for each individual snake body parts
class snake_parts:
    # constructor and attributes
    def __init__(self, head, x, y):
        # part can be head or not
        if head:
            self.head = True
        else:
            self.head = False
        self.x = x
        self.y = y

    # methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_head(self):
        return self.head

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


# class for snake object
class snake:
    def __init__(self):
        # object is made up of snake_parts objects
        self.snake_parts_list = []
        self.direction = "n"
        # creates head at starting position (9,9)
        self.snake_parts_list.append(snake_parts(True, 9, 9))

    # methods
    # movement method (decides movement of snake as a whole)
    def movement(self):
        # using temp list we set the next position of each part to the previous position of snake part before it
        # so [head,body1,body2] the position of body2 would be set to body1, body1 to head and head position is
        # calculated  in the next part
        temp = self.snake_parts_list
        tempx = []
        tempy = []
        for i in temp:
            tempx.append(i.get_x())
            tempy.append(i.get_y())
        for i in range(1, len(temp)):
            self.snake_parts_list[i].set_y(tempy[i - 1])
            self.snake_parts_list[i].set_x(tempx[i - 1])
        # the next position of the head is decided by the value of the direction attribute
        # if up is pressed then the snake will move 'n' or up until another key is pressed
        if self.direction == "n":
            self.snake_parts_list[0].set_y(int(self.snake_parts_list[0].get_y()) - 1)
            # allows snake to wraparound play area
            if self.snake_parts_list[0].get_y() == -1:
                self.snake_parts_list[0].set_y(19)
        elif self.direction == "e":
            self.snake_parts_list[0].set_x(int(self.snake_parts_list[0].get_x()) + 1)
            if self.snake_parts_list[0].get_x() == 20:
                self.snake_parts_list[0].set_x(0)
        elif self.direction == "s":
            self.snake_parts_list[0].set_y(int(self.snake_parts_list[0].get_y()) + 1)
            if self.snake_parts_list[0].get_y() == 20:
                self.snake_parts_list[0].set_y(0)
        elif self.direction == "w":
            self.snake_parts_list[0].set_x(int(self.snake_parts_list[0].get_x()) - 1)
            if self.snake_parts_list[0].get_x() == -1:
                self.snake_parts_list[0].set_x(19)

    # grow method
    def grow(self):
        # finds position of end piece and adds piece after it when next movement is made
        end = len(self.snake_parts_list) - 1
        x = self.snake_parts_list[end].get_x()
        y = self.snake_parts_list[end].get_y()
        self.snake_parts_list.append(snake_parts(False, x, y))

    def set_direction(self, dir):
        # sets direction to passed parameter
        self.direction = dir

    # keyboard control method
    def control(self, prev_dir):
        # based on what key is pressed the snake moves N or E or S or W
        if keyboard.is_pressed("up"):
            # the snake cant move back, only forwards left or right
            if self.direction != "s":
                return "n"
            # if the user tries moving the head into the part behind i.e presses up whilst the snake is directed south
            # south is returned as the user has made an invalid move
            else:
                return prev_dir
        elif keyboard.is_pressed("down"):
            if self.direction != "n":
                return "s"
            else:
                return prev_dir
        elif keyboard.is_pressed("left"):
            if self.direction != "e":
                return "w"
            else:
                return prev_dir
        elif keyboard.is_pressed("right"):
            if self.direction != "w":
                return "e"
            else:
                return prev_dir
        else:
            return prev_dir


# apple class
class apple:
    # constructor initialises random x and y coordinates in play area for apple to appear
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

    # method for new position
    def new_pos(self, snakes):
        # if random coordinates are the same as coordinates of a snake part the new coordinates are generated, recursive
        for i in snakes:
            if (i.get_x(), i.get_y()) == (self.x, self.y):
                self.x = random.randint(0, 19)
                self.y = random.randint(0, 19)
                self.new_pos(snakes)
