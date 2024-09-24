import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name")
    answer = answer_state.lower()

    if answer_state.lower() == "exit":
        missing_states = []
        for state in data.state:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in data["state"]:
        if answer == state.lower():
            show_answer = turtle.Turtle()
            nam_state = data[data.state == state]
            x_coord = nam_state.x
            y_coord = nam_state.y
            correct_guesses.append(state)
            score += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x_coord), int(y_coord))
            t.write(state)
