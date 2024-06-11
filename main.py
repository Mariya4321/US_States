import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_50 = pandas.read_csv("50_states.csv")
lst = state_50.state.to_list()
score = 0
guess = []
while len(guess) < 50:
    answer_state = screen.textinput(title=f"Guess {score}/50 state", prompt="What's the another state name?").capitalize()
    if answer_state == 'Exit':
        missing_state = [state for state in lst if state not in guess]
        # for state in lst:
        #     if state not in guess:
        #         missing_state.append(state)
        not_guess = pandas.DataFrame(missing_state)
        not_guess.to_csv("NotGuessState")
        break
    if answer_state in lst:
        guess.append(answer_state)
        row = state_50[state_50.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(row.x), int(row.y))
        t.write(row.state.item())
        score += 1



