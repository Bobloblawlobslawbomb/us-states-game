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

correct_guesses = 0

while correct_guesses < 50:
    answer_state = screen.textinput(
        title=f"{correct_guesses}/50 States",
        prompt="What's another states' name?"
    ).title()
    if answer_state == "Exit":
        with open("states_to_learn.csv", mode="w") as file:
            for state in states_list:
                file.write(state[0])
                file.write("\n")
        break
    for item in states_list:
        state_name = str(item[0])
        state_x = int(item[1])
        state_y = int(item[2])
        if answer_state == state_name:
            turtlewriter.update_map(state_x, state_y, state_name)
            correct_guesses += 1
            states_list.remove(item)

turtle.mainloop()


# import pandas
# import turtle


# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "./blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("50_states.csv")
# all_states = data.state.tolist()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(
#         title=f"{len(guessed_states)}/50 States",
#         prompt="What's another states' name?"
#     ).title()

#     if answer_state == "Exit":
#       break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(state_data.state.item())

# states_to_learn.csv

# screen.exitonclick()
