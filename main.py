# Imports
import turtle as trtl
import random as rand
import threading

# Init. turtle stuff
wn = trtl.Screen()
wn.bgcolor('black')
# Add images
blocksImg = "img/green.gif"
playerImg = "img/paddle.gif"
ballImg = "img/ball.gif"
wn.addshape(blocksImg)
wn.addshape("img/yellow.gif")
wn.addshape("img/red.gif")
wn.addshape(playerImg)
wn.addshape(ballImg)

# Init global variables before start
blocks = []
blocksX = []
blocksY = []
blocksWd = 30
blocksHt = 10
blocksGap = 10
blocksNumX = 7
blocksNumY = 3

plyMoving = False
running = False

# Functions
def spawnBlock(): # Spawn and initialize blocks
  block = trtl.Turtle()
  block.shape(blocksImg)
  block.penup()
  block.speed(0)
  blocks.append(block)
 
def gameSpawn():
    global blocksWd, blocksHt, blocksGap, blocksNumX, blocksNumY
    totalWd = (blocksNumX*blocksWd)+((blocksNumX-1)*blocksGap)
    totalHt = (blocksNumY*blocksHt)+((blocksNumY-1)*blocksGap)
    incrementX=blocksWd+blocksGap
    incrementY=blocksHt+blocksGap
    currentX=(-totalWd)/2
    currentY=((-totalHt)/2)+500
    currentX+=blocksWd/2
    currentY+=blocksHt/2
    counterX=0
    counterY=0
    while counterY<3:
        counterY+=1
        currentY+=incrementY
        if counterY==0:
            currentShape="img/green.gif"
        elif counterY==1:
            currentShape="img/yellow.gif"
        elif counterY==2:
            currentShape="img/red.gif"
        while counterX<7:
            counterX+=1
            blockName=str(counterX),str(counterY)
            blockName=trtl.Turtle
            blockName.goto(currentX,currentY)
            blockName.shape(currentShape)
            currentX+=incrementX
        currentX=(-totalWd)/2
        currentX+=blocksWd/2

def moveBall():
  running = True
  while (True and running):
    if (plyMoving):
      ball.forward(4)
      print(plyMoving)
    else:
      ball.forward(2)
      print(plyMoving)
runBall = threading.Thread(target=moveBall)

def paddleLeft(): # Move player left and right
  ply.goto(ply.xcor()-15,ply.ycor())
  if (running == False):
    runBall.start()
def paddleRight():
  ply.goto(ply.xcor()+15,ply.ycor())
  if (running == False):
    runBall.start()
def releaseKey():
  global plyMoving
  plyMoving = False


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
dir = rand.randint(0,1)
if (dir == 0):
  ball.left(45)
  plyMoving = True
elif (dir == 1):
  ball.left(135)
  plyMoving = True

wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")
wn.onkeyrelease(releaseKey, "a")
wn.onkeyrelease(releaseKey, "d")
wn.onkeyrelease(releaseKey, "Left")
wn.onkeyrelease(releaseKey, "Right")

wn.listen()
wn.mainloop()
