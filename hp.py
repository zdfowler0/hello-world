import turtle as trtl
 
# Import libraries
import turtle as trtl
import random
wn = trtl.Screen()
wn.bgcolor("lightseagreen")
wn.title("Hungry Hungry Turtles")
 
# Distance the turtles are from the center
pos = 175
# Number of balls 
ball_count = 17
 
#Create boundaries
bt = trtl.Turtle()
bt.penup()
bt.setposition(-pos, -pos)
bt.speed(0)
bt.width(15)
bt.pencolor("white")
bt.pendown()
for i in range(4):
  bt.forward(2*pos)
  bt.left(90)
bt.hideturtle()
 
hippos = []
 
# Creates turtles(hippos)
red = trtl.Turtle()
red.turtlesize(3.5)
red.color("firebrick")
red.penup()
red.shape("turtle")
red.speed(0)
red.goto(-pos,0)
hippos.append(red)
red_score = []
 
blue = trtl.Turtle()
blue.turtlesize(3.5)
blue.color("darkviolet")
blue.penup()
blue.shape("turtle")
blue.setheading(180)
blue.speed(0)
blue.goto(pos,0)
hippos.append(blue)
blue_score = []
 
yellow = trtl.Turtle()
yellow.turtlesize(3.5)
yellow.color("goldenrod")
yellow.penup()
yellow.shape("turtle")
yellow.setheading(270)
yellow.speed(0)
yellow.goto(0,pos)
hippos.append(yellow)
yellow_score = []
 
green = trtl.Turtle()
green.turtlesize(3.5)
green.color("green")
green.penup()
green.shape("turtle")
green.setheading(90)
green.speed(0)
green.goto(0,-pos)
hippos.append(green)
green_score = []
 
# List to store balls in
balls = []
 
# Colors for the balls
#ball_colors = ["red", "blue", "lime", "yellow"]
ball_colors = ["red","royalblue","yellow","lime"]
 
# Creates the balls
for i in range(ball_count):
  ball = trtl.Turtle()
  ball.hideturtle()
  ball.shape("circle")
  ball.color(ball_colors[random.randint(0, (len(ball_colors)-1))])
  balls.append(ball)
  ball.penup()
  ball.turtlesize(0.5)
  ball.speed(0)
 
# Places balls in the corners
location = 0
for ball in balls:
  if (0 <= location <= 1*((ball_count-1)/4)):
    ball.goto(pos-15,pos-15)
    ball.setheading(random.randint(210, 250))
  elif (1*((ball_count-1)/4) < location <= 2*((ball_count-1)/4)):
    ball.goto(-pos+15,pos-15)
    ball.setheading(random.randint(300, 330))
  elif (2*((ball_count-1)/4) < location <= 3*((ball_count-1)/4)):
    ball.goto(-pos+15,-pos+15)
    ball.setheading(random.randint(30, 60))
  elif (3*((ball_count-1)/4) < location <= 4*((ball_count-1)/4)):
    ball.goto(pos-15,-pos+15)
    ball.setheading(random.randint(120, 150))
  ball.showturtle()
  location += 1
 
 
ball_speed = 23
def move_balls():
  for ball in balls:
    if (abs(ball.xcor()) >= pos-10 or abs(ball.ycor()) >= pos-10):
      ball.setheading(ball.heading() + random.randint(160,200))
      ball.forward(ball_speed*1.2)
    else:
      ball.forward(ball_speed)
 
def eat_balls(turtle):
  for ball in balls:
    if (turtle.xcor() - 15 <= ball.xcor() <= turtle.xcor() + 15) and (turtle.xcor() - 15 <= ball.xcor() <= turtle.xcor() + 15):
      if turtle == hippos[0]:
        red_score.append(ball)
        ball.setpos(-2*pos,0)
        balls.remove(ball)
      if turtle == hippos[1]:
        blue_score.append(ball)
        ball.setpos(2*pos,0)
        balls.remove(ball)
      if turtle == hippos[2]:
        yellow_score.append(ball)
        ball.setpos(0,2*pos)
        balls.remove(ball)
      if turtle == hippos[3]:
        green_score.append(ball)
        ball.setpos(0,-2*pos)
        balls.remove(ball)
 
# Actually moves Hippos
for j in range(4):
  hippos[j].speed(5)
 
def red():
  hippos[0].forward(30)
  eat_balls(hippos[0])
  hippos[0].setx(-pos)
 
def blue():
  hippos[1].forward(30)
  eat_balls(hippos[1])
  hippos[1].setx(pos)
 
def yellow():
  hippos[2].forward(30)
  eat_balls(hippos[2])
  hippos[2].sety(pos)
 
def green():
  hippos[3].forward(30)
  eat_balls(hippos[3])
  hippos[3].sety(-pos)
 
#listen for keypresses
def listening():
  wn.listen()
  wn.onkey(green, 'n')
  wn.onkey(yellow, 'c')
  wn.onkey(blue, 'p')
  wn.onkey(red, "`")
 
i = 1
# main game loop
while (len(balls) != 0):
  move_balls()
  # Does function listening() whenever i / 4 has no remainder
  if ((i%4) == 0):
    listening()
  i += 1
 
wn.mainloop()