from cmu_graphics import *
import random
# Wordle

app.words = ['Castle','Spirit','Potato','Rocket','Window','Basket']
app.word = random.choice(app.words)
print(app.word)

app.characters = [' ',' ',' ',' ',' ',' ']
# app.characters = ['_', '_', '_', '_', '_', '_']
app.row = 1

firstRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 60, fill='black', size=30)
secondRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 100, fill='black', size=30)
thirdRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 140, fill='black', size=30)
fourthRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 180, fill='black', size=30)
fifthRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 220, fill='black', size=30)
sixthRow = Label(app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5], 200, 260, fill='black', size=30)

lenWord = len(app.word)
correctLetters = 0

def update(row):
    if row == 1:
        firstRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
    if row == 2:
        secondRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
    if row == 3:
        thirdRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
    if row == 4:
        fourthRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
    if row == 5:
        fifthRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
    if row == 6:
        sixthRow.value = app.characters[0] + '   ' + app.characters[1] + '   ' + app.characters[2] + '   ' + app.characters[3] + '   ' + app.characters[4] + '   ' + app.characters[5]
     

Grid = Group(
    Rect(80,40,240,240, fill=None, border='black'),
    Line(120,40,120,280),
    Line(160,40,160,280),
    Line(200,40,200,280),
    Line(240,40,240,280),
    Line(280,40,280,280),
    Line(80,80,320,80),
    Line(80,120,320,120),
    Line(80,160,320,160),
    Line(80,200,320,200),
    Line(80,240,320,240))

while correctLetters != lenWord:
    userInput = app.getTextInput("Guess a word:")

cmu_graphics.run()