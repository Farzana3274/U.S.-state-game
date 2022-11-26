import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_state = []

data = pandas.read_csv("50_states.csv")
# print(data)
all_state = data.state.to_list()

while len(guess_state) < 50:
    user_prompt = screen.textinput(f"{len(guess_state)}/50 Correct State.", "Enter state name. ").title()
    if user_prompt == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    if user_prompt in all_state:
        guess_state.append(user_prompt)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_prompt]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_prompt)


