from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import BooleanProperty

from statusbar import StatusBar
from square import Square

class Play(Button):
    def start(self, instance, *args):
        #Initialize EVERYTHING
        self.status_bar.game_start = False
        self.status_bar.player = "X"
        
        for child in self.board.children:
            if child.children != []:
                self.status_bar.counter -= 1            #Note that this will trigger on_counter -> end_game ->play.text
                                                        # being modified
                child.remove_widget(child.children[0])
                child.filled = False
                child.value = None
                
        self.text = "Wait"  # Put this after the ...counter-= 1 part to ensure
                            # this is the final text
        self.status_bar.turn.text = "Game start!"
        Clock.schedule_once(self.startBool,1)

    def startBool(self, dt): #this is to match the scheduled func where timeout is also an argument
        self.text = "Play"
        self.status_bar.game_start = True
        


