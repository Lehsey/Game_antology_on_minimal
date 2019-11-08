from tkinter import Tk, Canvas, Label
import random
from Game_over import GameOver


class Snake_game:

    def __init__(self, game):
        # основные константы
        self.game = game
        self.Width = 800
        self.Height = 600
        self.Seg_size = 20
        self.In_game = True
        # окна и создание поля
        self.Back = Tk()
        self.Back.title('Питон на питоне')
        self.score = 0
        self.field = Canvas(self.Back, width=self.Width,
                            height=self.Height, bg="#003300")
        self.field.grid()
        self.field.focus_set()
        self.field.create_text(720, 570, text=f"управление через\n стрелочки",
                               font='Arial 10', fill='white')
        self.start_game()
        self.Back.mainloop()

    def start_game(self):
        # начало игры
        self.create_apple()
        self.s = self.create_snake()
        # обработка нажатия
        self.field.bind("<KeyPress>", self.s.change_direction)
        self.main()

    def create_snake(self):
        # создание кусков змеи
        segments = [Segment(self.Seg_size, self.Seg_size, self),
                    Segment(self.Seg_size * 2, self.Seg_size, self),
                    Segment(self.Seg_size * 3, self.Seg_size, self)]
        return Snake(segments)

    def create_apple(self):
        # создание яблок для поедания
        pos_x = self.Seg_size * random.randint(1, (self.Width - self.Seg_size)
                                               / self.Seg_size)
        pos_y = self.Seg_size * random.randint(1, (self.Height - self.Seg_size)
                                               / self.Seg_size)
        self.apple = self.field.create_oval(pos_x, pos_y,
                                            pos_x + self.Seg_size, pos_y + self.Seg_size, fill='red')

    def main(self):
        if self.In_game:
            self.s.move(self)
            head_coords = self.field.coords(self.s.parts[-1].part)
            x1, y1, x2, y2 = head_coords
            # проверка выполза за пределы
            if x2 > self.Width or x1 < 0 or y1 < 0 or y2 > self.Height:
                self.In_game = False
            # поедание яблок
            elif head_coords == self.field.coords(self.apple):
                self.score += 1
                self.s.add_segment(self)
                self.field.delete(self.apple)
                self.create_apple()
            # врезался в себя
            else:
                for i in range(len(self.s.parts) - 1):
                    if head_coords == self.field.coords(self.s.parts[i].part):
                        self.In_game = False
            self.Back.after(100, self.main)
        # проигрыш
        else:
            self.field.create_text(self.Width / 2, self.Height / 2, text="GAME OVER!",
                                   font='Arial 30', fill='red')
            self.field.create_text(self.Width / 2, self.Height / 3, text=f"Ваш счёт: {self.score}",
                                   font='Arial 20', fill='red')
            self.over = GameOver(self.game, self.score)
            self.over.show()



class Segment:
    # часть змеи
    def __init__(self, x, y, game):
        self.part = game.field.create_rectangle(x, y,
                                                x + game.Seg_size, y + game.Seg_size,
                                                fill="white")


class Snake:

    def __init__(self, parts):
        self.parts = parts
        # в какую сторону
        self.side = {"Down": (0, 1), "Right": (1, 0),
                     "Up": (0, -1), "Left": (-1, 0)}
        self.vector = self.side["Right"]

    def move(self, game):
        # движение змейки
        for i in range(len(self.parts) - 1):
            segment = self.parts[i].part
            x1, y1, x2, y2 = game.field.coords(self.parts[i + 1].part)
            game.field.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = game.field.coords(self.parts[-2].part)
        game.field.coords(self.parts[-1].part,
                          x1 + self.vector[0] * game.Seg_size, y1 +
                          self.vector[1] * game.Seg_size,
                          x2 + self.vector[0] * game.Seg_size, y2+self.vector[1] * game.Seg_size)

    def add_segment(self, game):
        # увеличиваем змейку
        last_seg = game.field.coords(self.parts[0].part)
        x = last_seg[2] - game.Seg_size
        y = last_seg[3] - game.Seg_size
        self.parts.insert(0, Segment(x, y, game))

    def change_direction(self, event):
        # изменение направления
        if event.keysym in self.side:
            self.vector = self.side[event.keysym]
