import turtle
import random
class Display:
    def __init__(self, screen=0):
        self.t = turtle.Turtle()
        self.scr = self.t.getscreen()
        self.scr.onclick(self.mouse_event)
        self.scr.listen()
        elements = []
    def mouse_event(self,x,y):
        radius = random.randint(10,100)
        color = random.choice(["blue", "red", "green"])
        mycircle = Circle(x, y, radius, color)
        mycircle.draw(self.t)
class Shape:
    def __init__ (self, x=0, y=0, color="#000000"):
        self.filled = False
        self.x = x
        self.y = y
        self.color = color
    def set_fill_color(self, color):
        self.fill_color = color
    def set_filled(self, filled):
        self.filled = filled
    def is_filled(self):
        return self.filled
class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1, color="#000000"):
        self.filled = False
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self, t):
        t.penup()
        t.goto(self.x,self.y)
        t.circle(self.radius)
        t.pendown()
        t.circle(self.radius)
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()
Call = Display()
