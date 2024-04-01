from cmu_graphics import *
playershield = Polygon(30,30,60,30,60,63,45,70,30,63, border='black', fill='gold', opacity = 50)
playercont = Circle(200,200,10,fill='dodgerBlue', border='blue')

playershield.centerX = playercont.centerX
playershield.centerY = playercont.centerY
player = Group(playercont,playershield)

player.dx = 0
player.dy = 0

playershield.visible = False
enemy = Circle(200,100,10,fill='white', border='gray')
ball = Circle(200,0,12, fill='red', border='darkRed')
ball.speed = 1.5
ball.dx = 0
ball.dy = 0

app.stepsPerSecond=60

player.block = False
player.blockCD = False
enemy.block = False

player.blockseconds = 0

app.target = player

def onMousePress(x,y):
    if not player.blockCD == True:
        playershield.visible = True
        player.block = True
        player.blockCD = True
import random

def onKeyHold(keys):
    if ('w' in keys):
        if player.centerY - 2 >15:
            player.centerY -= 2 
            playershield.centerX = player.centerX
            playershield.centerY = player.centerY
        else: 
            player.dy = 0
    if ('s' in keys):
        if player.centerY + 2 <385:
            player.centerY +=2 
            playershield.centerX = player.centerX
            playershield.centerY = player.centerY
        else:
            player.dy = 0
    if ('a' in keys):
        if player.centerX -2 >14:
            player.centerX -=2
            playershield.centerX = player.centerX
            playershield.centerY = player.centerY
        else: 
            player.dy = 0
    if ('d' in keys):
        if player.centerX +2 <385:
            player.centerX += 2
            playershield.centerX = player.centerX
            playershield.centerY = player.centerY
        else:
            player.dx = 0
            
def onKeyPress(key):
    if key == 'f':
        if not player.blockCD == True:
            playershield.visible = True
            player.block = True
            player.blockCD = True
    if key =='q':
        print('dash')
        
def onMouseRelease(x,y):
   player.block = False
   playershield.visible = False

def EndGame(message):
    Label(message,200,200,size=20)
    app.stop()
    
def onStep():
    dist = distance(ball.centerX,ball.centerY,player.centerX,player.centerY)
    getPointInDir(ball.centerX, ball.centerY, player.centerX, player.centerY)
    
    face = angleTo(ball.centerX, ball.centerY, app.target.centerX, app.target.centerY)
    facex, facey = getPointInDir(ball.centerX, ball.centerY, face, 2*ball.speed)
    
    Xdist = ball.centerX-player.centerX
    Ydist = ball.centerY-player.centerY
    
    if app.target ==enemy:
        blocker = random.randint(80,150,)
        if blocker >=120:
            enemy.block = True
    else:
        enemy.block = False
        
    ball.dx = facex
    ball.dy = facey
    
    ball.centerX = ball.dx
    ball.centerY = ball.dy
    
    if player.blockCD == True:
        player.blockseconds +=1
        if player.blockseconds >=90:
            player.block = False
            playershield.visible = False
    if player.blockseconds >=160 or player.blockCD == False:
        player.blockseconds = 0 
        player.blockCD = False
    if ball.hits(app.target.centerX,app.target.centerY):
        if app.target.block == False:
            if app.target == player:
                EndGame('Enemy Wins!')
            elif app.target == enemy:
                EndGame('Player Wins!') 
        elif app.target.block == True:
            ball.speed +=.1
            if app.target ==player:
                app.target=enemy
                playershield.visible = False
                player.block = False
                player.blockCD = False
            elif app.target == enemy:
                app.target=player
                enemy.block = False
cmu_graphics.run()