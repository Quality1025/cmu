from cmu_graphics import *
app.background='black'

Title = Group(
    Rect(80,40,240,80, border='orangered', borderWidth=4, fill='white'),
    Label('SwordBurst', 200,80, size=25, fill=gradient('gold', 'red', start='left')))
Title.centerY=1000
    
# app.url= 'cmu://703726/27730945/Sword.png'
app.url="https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg"
Image(app.url, 85, 150, opacity=30,fill='orangered')

Start = Group(
    Label('Start', 400, 240, size=30, fill=gradient('orange', 'red', start='right')))

# Background Layout
second = Group(
    Rect(0,0,400,400, fill='white'))
second.visible=False

# Map Choose & Layout
app.Maps = ['forestgreen', 'skyblue', 'firebrick', 'mediumslateblue','purple']
app.level = 0

MButton = Rect(240,160,80,100, fill='dimgrey')

MapUp = Polygon(260,200,280,170,300,200, fill=gradient('silver', 'white'))
MapDown = Polygon(260,220,280,250,300,220, fill=gradient('silver', 'white'))

MapDown.visible=False
MapUp.visible=False
MButton.visible=False

Map = Group(
    Rect(40,120,160,160, fill='red'))
Map.visible=False

MChoose = Label('Choose Your Map',200, 40, size=35, fill=gradient('dodgerblue','mediumslateblue', 'blue', start='center'), font='Caveat')
MChoose.visible=False
# Ready Button 
Ready = Label('Ready', 200,320, fill=gradient('mediumslateblue','blue','aqua'), size=30, font='caveat')
Ready.visible=False


def onMousePress (mouseX, mouseY):
    if Start.contains(mouseX, mouseY):
        second.visible=True
        MapUp.visible=True
        MButton.visible=True
        MapDown.visible=True
        Map.visible=True
        MChoose.visible=True
        Ready.visible=True
    # if (MapUp.hits(mouseX, mouseY)):
    #     app.Map+=1
    #     if (app.Map ==6):
    #         app.Map = 0
    #     Map.fill=app.Maps[app.Map]
    if (MapUp.hits(mouseX, mouseY)):
        app.level += 1
        if (app.level == 5):
            app.level = 0
        Map.fill=app.Maps[app.level]

    # if (MapDown.hits(mouseX, mouseY)):
    #     app.Map-=1
    #     Map.fill=app.Maps[app.Map]
    #     if (app.Map==0):
    #         app.Map = 6
    #           if Ready.contains(mouseX, mouseY):
    #            app.background='white'
    if (MapDown.hits(mouseX, mouseY)):
        app.level -= 1
        if (app.level == 5):
            app.level = 0
        Map.fill=app.Maps[app.level]

    def redMap():
        print("red")
    def blueMap():
        print("Blue")
    
    if Ready.contains(mouseX, mouseY):
        MChoose.visible = False
        Ready.visible = False
        if Map.fill == 'red':
            redMap()
        if Map.fill == 'skyblue':
            print("Blue")
        if Map.fill == 'forestgreen':
            print("forestgreen")
        if Map.fill == 'firebrick':
            print("firebrick")
        if Map.fill =='mediumslateblue':
            print("mediumslateblue")
        if Map.fill =='purple':
            print("purple")

        Map.visible = False
        MapUp.visible = False
        MapDown.visible = False
        MButton.visible = False
    
    
  
def onStep():
    if Title.centerY - 10 > 80:
        Title.centerY -=15
    if Start.centerX - 1 > 200:
        Start.centerX -=5

cmu_graphics.run()