import os

from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.uix.label import Label, Widget
from kivy.graphics import Rectangle, Color, Ellipse, Line
from  kivy.uix.image import Image
from kivy.vector import Vector


class Tile(Widget):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.resource = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', 'block_1.png')
        self.x = x
        self.y = y

    def draw(self):
        with self.canvas:
            Rectangle(source=self.resource, pos=(self.x, self.y))


class Character(Widget):
    def __init__(self):
        super().__init__()
        self.is_selected = False
        self.x = 20
        self.y = 10

    def draw(self):
        self.r = 0 if self.is_selected else 1
        with self.canvas:
            Ellipse(pos=(self.x, self.y), size=(70, 20), color=Color(self.r,1,1))

    def on_touch_down(self, touch):
        self.is_selected = not self.is_selected
        print(touch)


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, dt):
        for children in self.children:
            children.draw()


class MyApp(App):
    def build(self):
        character = Character()
        game = Game()
        game.add_widget(character)
        self.draw_background(game)
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

    def draw_background(self, game):
        TILE_SIZE = 100

        map = [[1,0,1],
               [0,1,0]]

        # `reverse` to draw map on canvas as it seen in code.
        for y, row in enumerate(reversed(map)):
            for x, tile in enumerate(row):
                if tile == 1:
                    game.add_widget(Tile(x=x*TILE_SIZE, y=y*TILE_SIZE))


if __name__ == '__main__':
    MyApp().run()