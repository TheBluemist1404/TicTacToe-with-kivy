from kivy.uix.gridlayout import GridLayout
from square import Square

from kivy.properties import NumericProperty

class Board(GridLayout):
    counter = 0
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 4
        for x in range(0, 9):
            sq = Square()
            self.add_widget(sq)

