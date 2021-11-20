import turtle
import csv
from turtlewriter import TurtleWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("./blank_states_img.gif")

turtlewriter = TurtleWriter()

with open("50_states.csv", newline='') as csv_file:
    states_list = []
    data = csv.reader(csv_file)
    for row in data:
        states_list.append(row)
states_list.pop(0)

game_on = True
correct_guesses = 0

while game_on:
    answer_state = screen.textinput(
        title=f"{correct_guesses}/50 States",
        prompt="What's another states' name?"
    )

    for item in states_list:
        state_name = str(item[0])
        state_x = int(item[1])
        state_y = int(item[2])
        if answer_state.lower() == state_name.lower():
            turtlewriter.update_map(state_x, state_y, state_name)
            correct_guesses += 1

turtle.mainloop()
