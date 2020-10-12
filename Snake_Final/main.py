# import needed modules
import tkinter as tk
from tkinter import messagebox
import logic as log
import sys

# creates snake and apple object
s = log.snake()
a = log.apple()


# main app class
class App(tk.Tk):
    # creates tkinter window
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # creates a canvas on which game is displayed
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cell_width = 25
        self.cell_height = 25
        self.rect = {}
        self.oval = {}
        self.turns = 0
        # creates grid needed for displaying snake and apple
        for column in range(20):
            for row in range(20):
                x1 = column * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.rect[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="rect")
                self.oval[row, column] = self.canvas.create_oval(x1 + 2, y1 + 2, x2 - 2, y2 - 2, fill="black",
                                                                 tags="oval")
                self.canvas.itemconfig(self.oval[row, column], state="hidden")
        # new position for apple is generated
        a.new_pos(s.snake_parts_list)
        # snake is given head and 2 body parts to start with
        s.grow()
        s.grow()
        # set speed at which game runs, delay of 100ms before updating
        self.re_draw(100)

    # class for drawing snake and apple positions
    def re_draw(self, delay):
        # sets every rectangle to black to start with
        for y in range(0, 20):
            for x in range(0, 20):
                self.canvas.itemconfig(self.rect[y, x], fill="black")
        # runs game play function, sets new snake position
        self.game_play()
        # sets the oval at specified coordinates to show an apple based on apple objects coordinates
        self.canvas.itemconfig(self.oval[a.y, a.x], state="normal", fill="green")
        # draws orange rectangle for head and red  for body part, loops through each part
        to_draw = []
        for i in s.snake_parts_list:
            to_draw.append((self.rect[i.get_y(), i.get_x()], i.is_head()))
        for i in to_draw:
            if i[1]:
                self.canvas.itemconfig(i[0], fill="orange")
            else:
                self.canvas.itemconfig(i[0], fill="red")
        # recursively runs re_draw method after specified delay in ms
        self.after(delay, lambda: self.re_draw(delay))

    # game play method
    def game_play(self):
        # due to bug of the game registering a death at the start the turns attributes is used
        self.turns += 1
        head_x = s.snake_parts_list[0].get_x()
        head_y = s.snake_parts_list[0].get_y()
        # if at any point the head coordinates are equal to apple coordinates the snake grows and new apple position
        # is generated
        if (head_x, head_y) == (a.x, a.y):
            self.canvas.itemconfig(self.oval[a.y, a.x], state="hidden", fill="black")
            a.new_pos(s.snake_parts_list)
            s.grow()
        # checks through every body part of snake if the head and body part have equal coordinates
        for i in range(1, len(s.snake_parts_list)):
            if self.turns > 1:
                if (s.snake_parts_list[i].get_x(), s.snake_parts_list[i].get_y()) == (head_x, head_y):
                    # if yes the game is over as the snake has died and the exit_application method runs
                    self.exit_application()
                    break
        # direction is determined
        s.direction = s.control(s.direction)
        # snake moves with movement method
        s.movement()

    def exit_application(self):
        # displays ask question message box with the answers yes or no
        # score is displayed and is user is asked is they want to play again
        msg_box = messagebox.askquestion("Game Over",
                                         'Do you want to play again?' + '\n' + (
                                                 "You Scored: " + str(len(s.snake_parts_list) - 1)),
                                         icon='warning')
        # if they choose to play again
        if msg_box == 'yes':
            # all variables and lists used are reset to their defaults and the game starts from the beginning
            self.turns = 0
            self.deiconify()
            s.snake_parts_list = []
            s.direction = "n"
            s.snake_parts_list.append(log.snake_parts(True, 9, 9))
            a.new_pos(s.snake_parts_list)
            s.grow()
            s.grow()
            a.new_pos(s.snake_parts_list)

        else:
            # otherwise the script closes down
            sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
