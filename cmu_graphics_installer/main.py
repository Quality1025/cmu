from cmu_graphics import *
# Wordle

app.words = ['Castle','Spirit','Potato','Rocket','Window','Basket']


#app.characters = [' ',' ',' ',' ',' ',' ']
app.characters = ['_', '_', '_', '_', '_', '_']

l = Label(app.characters[0] + '     ' + app.characters[1] + '     ' + app.characters[2] + '     ' + app.characters[3] + '     ' + app.characters[4] + '     ' + app.characters[5], 195, 77, fill='white', size=30)

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

cmu_graphics.run()