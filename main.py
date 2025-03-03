#Imports
import turtle as trtl
import random as rand
import threading

# Init. turtle stuff
wn = trtl.Screen()
wn.bgcolor('black')
# Add images
blocksGreen = "img/green.gif"
blocksYellow = "img/yellow.gif"
blocksRed = "img/red.gif"
playerImg = "img/paddle.gif"
ballImg = "img/ball.gif"
wn.addshape(blocksGreen)
wn.addshape(blocksYellow)
wn.addshape(blocksRed)
wn.addshape(playerImg)
wn.addshape(ballImg)

# Init global variables before start
blocks = []
blocksWd = 50
blocksHt = 20
blocksGap = 4
blocksNumX = 17
blocksNumY = 5

ballSpeed = 6

started = False

# Functions
def gameSpawn(): # Spawn blocks and stuff
    global blocksWd, blocksHt, blocksGap, blocksNumX, blocksNumY
    totalWd = (blocksNumX*blocksWd)+((blocksNumX-1)*blocksGap)
    totalHt = (blocksNumY*blocksHt)+((blocksNumY-1)*blocksGap)
    incrementX=blocksWd+blocksGap
    incrementY=blocksHt+blocksGap
    currentX=(-totalWd)/2
    currentY=((-totalHt)/2)+200
    currentX+=blocksWd/2
    currentY+=blocksHt/2
    counterX=0
    counterY=0
    while counterY<blocksNumY:
      if counterY==0:
          currentShape = blocksRed
      elif counterY==2:
          currentShape = blocksYellow
      elif counterY==4:
          currentShape = blocksGreen
      while counterX<blocksNumX:
          block=trtl.Turtle()
          blocks.append(block)
          block.speed(0)
          block.penup()
          block.goto(currentX,currentY)
          block.shape(currentShape)
          currentX+=incrementX
          counterX+=1
      currentX=(-totalWd)/2
      currentX+=blocksWd/2
      currentY+=incrementY
      counterX=0
      counterY+=1

deaths=0
daed=trtl.Turtle()
daed.hideturtle()
daed.goto(-100,-300)
daed.write("Lives lost: " + str(deaths), ["Red", 20, "Aerial"])
def death():
    daed.goto(-100,-300)
    global deaths,fonta
    daed.clear()
    ball.setheading(0)
    ball.left(rand.randint(30,150))
    ball.goto(ply.xcor(),-290)
    deaths+=1
    daed.write("Lives lost: " + str(deaths), ["Red", 20, "Aerial"])

def ballCollideH():
  degree = (180-ball.heading())*2
  ball.setheading(ball.heading()+degree)
  ball.forward(10)
def ballCollideV():
  degree = (90-ball.heading())*2
  ball.setheading(ball.heading()+degree)
  ball.forward(12)
def moveBall(): # Move ball, called constantly
  global started
  started = True
  while True:
    for i in range(len(blocks)):
      if ball.xcor() < ply.xcor()-30 + 60 and\
          ball.xcor() + 10 > ply.xcor()-30 and\
          ball.ycor() < ply.ycor() + 10 and\
          ball.ycor() + 10 > ply.ycor():
        ballCollideH()
      elif ball.xcor() < blocks[i].xcor()-25 + 50 and\
          ball.xcor() + 10 > blocks[i].xcor()-25 and\
          ball.ycor() < blocks[i].ycor() + 20 and\
          ball.ycor() + 10 > blocks[i].ycor():
        if (blocks[i].shape() == "img/red.gif"):
          blocks[i].goto(1000,1000)
        elif (blocks[i].shape() == "img/yellow.gif"):
          blocks[i].shape("img/red.gif")
        elif (blocks[i].shape() == "img/green.gif"):
          blocks[i].shape("img/yellow.gif")
        ballCollideH()
    if ball.xcor()<-475:
      ballCollideV()
    elif ball.xcor()>475:
      ballCollideV()
    elif ball.ycor()>380:
      ballCollideH()
    elif ball.ycor()<-500:
        death()
    ball.forward(ballSpeed)
runBall = threading.Thread(target=moveBall)

def paddleLeft(): # Move player left and right
  if (started == False):
    runBall.start()
  if (ply.xcor() != -450):
    ply.goto(ply.xcor()-30,ply.ycor())
  ball.forward(ballSpeed*2)
def paddleRight():
  if (started == False):
    runBall.start()
  if (ply.xcor() != 450):
    ply.goto(ply.xcor()+30,ply.ycor())
  ball.forward(ballSpeed*2)


border = trtl.Turtle()
border.pencolor("white")
border.pensize(8)
border.penup()
border.speed(0)
border.setpos(-482, -500)
border.pendown()
border.left(90)
border.forward(908)
border.right(90)
border.forward(960)
border.right(90)
border.forward(1000)

ply = trtl.Turtle()
ply.shape(playerImg)
ply.penup()
ply.speed(0)
ply.setpos(ply.xcor(), -300)

ball = trtl.Turtle()
ball.shape(ballImg)
ball.penup()
ball.speed(0)
ball.setpos(ply.xcor(), -290)
ball.left(rand.randint(30,150))

gameSpawn()

wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")

wn.listen()
wn.mainloop()
