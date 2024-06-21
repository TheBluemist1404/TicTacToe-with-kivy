from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

from board import Board
from play import Play
# Load the KV file

Builder.load_file('square.kv')
Builder.load_file('tic_tac_toe.kv')
Builder.load_file('statusbar.kv')

class Tic_tac_toe(BoxLayout):
    pass

class TicTacToeApp(App):
    def build(self):
        return Tic_tac_toe()

if __name__ == '__main__':
    TicTacToeApp().run()
