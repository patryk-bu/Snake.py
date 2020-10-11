import random
import keyboard


class snake_parts:
    def __init__(self, head, x, y):
        if head:
            self.head = True
        else:
            self.head = False
        self.x = x
        self.y = y

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


class snake:
    def __init__(self):
        self.snake_parts_list = []
        self.direction = "n"
        self.snake_parts_list.append(snake_parts(True, 9, 9))

    def movement(self):
        temp = self.snake_parts_list
        tempx = []
        tempy = []
        for i in temp:
            tempx.append(i.get_x())
            tempy.append(i.get_y())
        for i in range(1, len(temp)):
            self.snake_parts_list[i].set_y(tempy[i - 1])
            self.snake_parts_list[i].set_x(tempx[i - 1])

        if self.direction == "n":
            self.snake_parts_list[0].set_y(int(self.snake_parts_list[0].get_y()) - 1)
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

    def grow(self):
        end = len(self.snake_parts_list)-1
        x = self.snake_parts_list[end].get_x()
        y = self.snake_parts_list[end].get_y()
        self.snake_parts_list.append(snake_parts(False, x, y))

    def set_direction(self, dir):
        self.direction = dir

    def control(self, prev_dir):
        if keyboard.is_pressed("up"):
            if self.direction != "s":
                return "n"
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


class apple:
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

    def new_pos(self, snakes):
        for i in snakes:
            if (i.get_x(), i.get_y()) == (self.x, self.y):
                self.x = random.randint(0, 19)
                self.y = random.randint(0, 19)
                self.new_pos(snakes)



