from cmu_graphics import *

# Setting up the canvas
app.background = 'skyblue'

# Creating the tennis court
Court = Rect(50, 50, 300, 200, fill='green', border='white', borderWidth=2)
Net = Line(200, 50, 200, 250, fill="white", lineWidth=2)

# Creating the tennis ball
Ball = Circle(200, 150, 10, fill='white', border='black', borderWidth=1)

# Setting up initial ball movement
Ball.dx = 2
Ball.dy = 1

# Player 1 (Left side)
Player1 = Rect(50, 120, 10, 60, fill='white')
Player1_score = 0

# Player 2 (Right side)
Player2 = Rect(340, 120, 10, 60, fill='white')
Player2_score = 0

cmu_graphics.run()