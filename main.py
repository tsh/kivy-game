import os

from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.uix.label import Label, Widget
from kivy.graphics import Rectangle, Color, Ellipse, Line
from  kivy.uix.image import Image
from kivy.vector import Vector


class Tile(Widget):
    def __init__(self):
        super().__init__()
        self.resource = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', 'block_1.png')

    def draw(self):
        with self.canvas:
            Rectangle(source=self.resource, pos=(40, 22))


class Character(Widget):
    def draw(self):
        self.pos = (20,10)
        with self.canvas:
            Color(1, 1, 0)
            Ellipse(pos=self.pos, size=(70, 20))
            Ellipse(pos=[200, 200], size=(70, 20))


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, dt):
        for children in self.children:
            children.draw()


class MyApp(App):
    def build(self):
        tile = Tile()
        character = Character()
        game = Game()
        game.add_widget(tile)
        game.add_widget(character)
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    MyApp().run()