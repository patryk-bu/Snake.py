import tkinter as tk
from tkinter import messagebox
import logic as log
import sys

s = log.snake()
a = log.apple()


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cell_width = 25
        self.cell_height = 25
        self.rect = {}
        self.oval = {}
        self.dead = -1
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
        a.new_pos(s.snake_parts_list)
        s.grow()
        s.grow()
        self.re_draw(100)

    def re_draw(self, delay):
        for y in range(0, 20):
            for x in range(0, 20):
                self.canvas.itemconfig(self.rect[y, x], fill="black")
        self.game_play()
        self.canvas.itemconfig(self.oval[a.y, a.x], state="normal", fill="green")
        to_draw = []
        x = 0
        for i in s.snake_parts_list:
            to_draw.append((self.rect[i.get_y(), i.get_x()], i.is_head(), x))
            x += 1
        for i in to_draw:
            if i[1]:
                self.canvas.itemconfig(i[0], fill="orange")
            else:
                if i[2] % 2 != 0:
                    self.canvas.itemconfig(i[0], fill="blue")
                else:
                    self.canvas.itemconfig(i[0], fill="red")
        self.after(delay, lambda: self.re_draw(delay))

    def game_play(self):
        head_x = s.snake_parts_list[0].get_x()
        head_y = s.snake_parts_list[0].get_y()
        if (head_x, head_y) == (a.x, a.y):
            self.canvas.itemconfig(self.oval[a.y, a.x], state="hidden", fill="black")
            a.new_pos(s.snake_parts_list)
            s.grow()
        for i in range(1, len(s.snake_parts_list)):
            # print(str(i))
            if (s.snake_parts_list[i].get_x(), s.snake_parts_list[i].get_y()) == (head_x, head_y):
                self.dead += 1
                if self.dead == 2:
                    print("ATE: " + (str(i)))
                    self.dead = 0
                    s.snake_parts_list = []
                    s.direction = "n"
                    s.snake_parts_list.append(log.snake_parts(True, 9, 9))
                    s.grow()
                    s.grow()
                    a.new_pos(s.snake_parts_list)
                    break
            else:
                pass
        s.direction = s.control(s.direction)
        s.movement()

    """def exit_application(self):
        MsgBox = messagebox.askquestion("Game Over",
                                        'Do you want to play again?' + '\n' + (
                                                    "You Scored: " + str(len(s.snake_parts_list) - 1)),
                                        icon='warning')
        if MsgBox == 'yes':
            self.dead = 0
            self.deiconify()
            s.snake_parts_list = []
            s.direction = "n"
            s.snake_parts_list.append(log.snake_parts(True, 9, 9))
            a.new_pos(s.snake_parts_list)
            s.grow()
            s.grow()

        else:
            sys.exit()"""


if __name__ == "__main__":
    app = App()
    app.mainloop()
