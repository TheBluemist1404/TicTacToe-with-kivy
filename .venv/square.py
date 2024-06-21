from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import BooleanProperty


class char_O(Widget):
    def __init__(self, **kwargs):
        super(char_O, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas, parent=self.update_canvas)
        # if we 'draw' O at the __init__ state, self.parent. center will returns NoneType error

    def update_canvas(self, *args):
        self.canvas.clear()
        if self.parent:
            with self.canvas:
                Color(1, 0, 0, 1)
                Line(circle=(self.parent.center_x, self.parent.center_y, self.parent.width / 2), width=2)


class char_X(Widget):
    def __init__(self, **kwargs):
        super(char_X, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas, parent=self.update_canvas)
        # if we 'draw' O at the __init__ state, self.parent. center will returns NoneType error

    def update_canvas(self, *args):
        self.canvas.clear()
        if self.parent:
            with self.canvas:
                Color(0, 1, 0, 1)
                Line(points=(self.parent.center_x - self.parent.width / 2, self.parent.center_y - self.parent.height / 2,
                             self.parent.center_x + self.parent.width / 2, self.parent.center_y + self.parent.height / 2), width=2)
            with self.canvas:
                Color(0, 1, 0, 1)
                Line(points=(self.parent.center_x - self.parent.width / 2, self.parent.center_y + self.parent.height / 2,
                             self.parent.center_x + self.parent.width / 2, self.parent.center_y - self.parent.height / 2), width=2)


class Square(Button):
    def __init__(self, **kwargs):
        super(Square, self).__init__(**kwargs)
        self.filled = False
        self.value  = None

    def press(self, instance, *args):
        if not self.filled and self.parent.status_bar.game_start:
            if self.parent.status_bar.player == "O":
                self.add_widget(char_O())
                self.value = "O"
            else:
                self.add_widget(char_X())
                self.value = "X"
            self.parent.status_bar.counter += 1
            self.filled = True
