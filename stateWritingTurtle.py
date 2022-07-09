from turtle import Turtle

class StateTurtle(Turtle):
    def __init__(self):
        super(StateTurtle, self).__init__()
        self.remaining_time = 10 * 60
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, x, y):
        self.goto(x,y)
        self.write(state_name)