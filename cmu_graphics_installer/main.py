from cmu_graphics import *

GRID_SIZE = 3
CELL_SIZE = 400 / GRID_SIZE
WINDOW_SIZE = 400
filledCells = []

def createBoard(visible):
    board = []
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            cell = Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE, fill=rgb(232, 191, 146), border='black', borderWidth=2, visible=visible)
            row.append(cell)
        board.append(row)
    return board

def drawX(cell):
    padding = 20
    cell_x = cell.centerX - cell.width / 2 + padding
    cell_y = cell.centerY - cell.height / 2 + padding
    cell_width = cell.width - 2 * padding
    cell_height = cell.height - 2 * padding
    
    line1 = Line(cell_x, cell_y, cell_x + cell_width, cell_y + cell_height, lineWidth=2, fill='blue')
    line2 = Line(cell_x + cell_width, cell_y, cell_x, cell_y + cell_height, lineWidth=2, fill='blue')


def drawO(cell):
    padding = 20
    cell_x = cell.centerX - cell.width / 2 + padding
    cell_y = cell.centerY - cell.height / 2 + padding
    cell_width = cell.width - 2 * padding
    cell_height = cell.height - 2 * padding
    
    # Calculate radius based on half of the smaller dimension
    if cell_width < cell_height:
        radius = cell_width / 2
    else:
        radius = cell_height / 2
    
    circle = Circle(cell.centerX, cell.centerY, radius, fill=None, border='red', borderWidth=2)

def onMousePress(mouseX, mouseY):
    global turn, filledCells
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell = board[i][j]
            if cell.contains(mouseX, mouseY) and [i, j] not in filledCells:
                if turn == 'X':
                    drawX(cell)
                    turn = 'O'
                else:
                    drawO(cell)
                    turn = 'X'
                
                filledCells.append([i, j])

def main():
    global board, turn, filledCells
    board = createBoard(True)
    turn = 'X'
    filledCells = []

main()

cmu_graphics.run()