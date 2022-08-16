import turtle
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
        if self.filled == True:
            t.fillcolor(self.color)
            t.begin_fill()
            t.circle(self.radius)
            t.end_fill()
if __name__ == "__main__":
    t = turtle.Turtle()
    Call = Circle(2, 2, 3, "blue")
