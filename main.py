import pandas
from turtle import Screen
from stateWritingTurtle import StateTurtle
import time

score = 0

#set up screen
screen = Screen()
screen.title("The US States Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

#timer turtle set up
state_turtle = StateTurtle()

#data set up
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while score < 50:
    player_input = screen.textinput(f"{score}/50 guessed:", "Enter a state:").title()
    if player_input == "Exit":
        break
    if player_input in all_states:
        state_data = data[data.state == player_input]
        state_turtle.write_state(player_input, float(state_data.x), float(state_data.y))
        score += 1
        guessed_states.append(player_input)
    time.sleep(0.5)

#make csv of unguessed states
unguessed_states = []
for state in all_states:
    if state not in guessed_states:
        unguessed_states.append(state)
unguessed_states_data_frame = pandas.DataFrame(unguessed_states)
unguessed_states_csv = unguessed_states_data_frame.to_csv()

file = open("states_to_learn.csv", "w")
file.write(unguessed_states_csv)
file.close()

screen.exitonclick()



