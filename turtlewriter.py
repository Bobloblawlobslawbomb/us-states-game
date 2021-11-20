from turtle import Turtle


class TurtleWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.color = "black"
        self.penup()
        self.hideturtle()

    def update_map(self, x, y, state):
        self.goto(x, y)
        self.write(
            state,
            align="center",
            font=("Courier", 10, "bold")
        )
