from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

#Note: Layout and Button are EventDispatcher children, which is why we can use attribute to call them
class StatusBar(BoxLayout):  
    game_start = BooleanProperty(False)
    counter = NumericProperty(0)
    player = "X"
    lineup = [[0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

    def on_game_start(self, *args):
        if self.counter == 0:
             self.turn.text = "It is "+self.player+"'s turn"
    
    def on_counter(self, *args):
        children = self.board.children
        for lp in self.lineup:
            lst = [children[i].value for i in lp]
            if lst.count("X") == 3:
                self.turn.text = "X win"
                self.gameover()
                break
            elif lst.count("O") == 3:
                self.turn.text = "O win"
                self.gameover()
                break
            else:
                continue
        if self.counter < 9 and self.game_start is True:
            if self.counter % 2 == 0:
                self.player = "X"
            else:
                self.player = "O"
            self.turn.text = "It is " + self.player + "'s turn"
        else:
            self.gameover()

    def winner(self):
        pass

    def gameover(self):
        self.game_start = False
        if self.turn.text not in ["X win ", "O win"]:
            self.turn.text = "It is a tie!"




