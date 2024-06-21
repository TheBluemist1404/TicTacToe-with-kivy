from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import BooleanProperty

from statusbar import StatusBar
from square import Square

class Play(Button):
    def start(self, instance, *args):
        self.status_bar.turn.text = "Game start!"
        Clock.schedule_once(self.startBool,1)

    def startBool(self, dt): #this is to match the scheduled func where timeout is also an argument
        self.status_bar.game_start = True
        


