import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0  # Correct the spelling of 'highestscore'

# Snake bodies
bodies = []

# Creating the screen (canvas)
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=600, height=600)

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("score: 0 | highest score: 0", font=("Arial", 16, "normal"))

# Functions to control the snake
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling - Key mappings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
    s.update()  # Update the screen

    # Check collision with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        # Move the food to a new random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)  # Append new body of the snake to the body list

        # Increase the score
        score += 10

        # Change delay
        delay -= 0.001

        # Update the highest score
        if score > highestscore:
            highestscore = score

        # Update the scoreboard
        sb.clear()
        sb.write("score: {} | highest score: {}".format(score, highestscore), font=("Arial", 16, "normal"))

    # Move the snake's body
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake's body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            # Reset score
            score = 0
            delay = 0.1

            # Update the scoreboard
            sb.clear()
            sb.write("score: {} | highest score: {}".format(score, highestscore), font=("Arial", 16, "normal"))

    # Delay and update the screen
    time.sleep(delay)

s.mainloop()  # End of the game loop