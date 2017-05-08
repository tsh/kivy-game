import kivy

from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.uix.label import Label, Widget
from kivy.graphics import Rectangle, Color, Ellipse, Line
from kivy.vector import Vector


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def draw(self):
        self.pos = Vector(*self.velocity) + self.pos
        with self.canvas:
            Color(1, 1, 0)
            Ellipse(pos=self.pos, size=(70,20))
            Ellipse(pos=[200, 200], size=(70,20))


class PongGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, dt):
        for children in self.children:
            children.draw()



class MyApp(App):

    def build(self):
        ball = PongBall()
        game = PongGame()
        game.add_widget(ball)
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    MyApp().run()