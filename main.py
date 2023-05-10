import pygame
from settings import *
from writer import Writer

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
writer = Writer(screen, size = 24, color = WHITE)
writer.setText('Red Turn')
board = []
for row in range(NUMROWS):
    board.append([])
    for col in range(NUMCOLS):
        if row == 0 or row == 1:
            board[row].append(BLUE)
        elif row == NUMROWS - 1 or row == NUMROWS - 2:
            board[row].append(RED)
        else:
            board[row].append(None)

def update():
    removeAbandonded()
    checkForWin()

def checkForWin():
    for col in range(NUMCOLS):
        color1 = board[0][col]
        color2 = board[NUMROWS - 1][col]
        if color1 == RED:
            writer.setText('Red Wins!')
        elif color2 == BLUE:
            writer.setText('Blue Wins!')

def removeAbandonded():
    for row in range(NUMROWS):
        for col in range(NUMCOLS):
            color = board[row][col]
            if color != None:
                if isAbandoned(row, col, color) == True:
                    board[row][col] = None    

def isAbandoned(row, col, color):
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            if row + i >= 0 and row + i < NUMROWS and col + k >= 0 and col + k < NUMCOLS:
                neighborColor = board[row + i][col + k]
                if neighborColor == color and (i != 0 or k != 0):
                    return False
    return True
                                
                

def printBoard():
    for row in range(NUMROWS):
        for col in range(NUMCOLS):
            if board[row][col] != None:
                if board[row][col].color == RED:
                    print('R', end = ' ')
                else:
                    print('B', end = ' ')
            else:
                print('_', end = ' ')
        print()

def draw():
    screen.fill(BGCOLOR)
    for row in range(NUMROWS):
        for col in range(NUMCOLS):
            color = board[row][col]
            if color != None:
                pygame.draw.circle(screen, color, (col * TILESIZE + TILESIZE // 2,
                                            row * TILESIZE + TILESIZE // 2),
                                   TILESIZE // 3)
            rect = pygame.Rect(col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, BLACK, rect,
                             width = 2)
    writer.writeText(WIDTH - 100, 100)
    pygame.display.update()

def onMousePress(x, y):
    tileX = x // TILESIZE
    tileY = y // TILESIZE
    if tileX < NUMCOLS and tileY < NUMROWS:
        color = board[tileY][tileX]
        if color != None:
            if color == RED and writer.getText() == 'Red Turn':
                if board[tileY-1][tileX] != RED:
                    board[tileY - 1][tileX] = color
                    writer.setText('Blue Turn')
                    board[tileY][tileX] = None
            elif color == BLUE and writer.getText() == 'Blue Turn':
                if board[tileY+1][tileX] != BLUE:
                    board[tileY + 1][tileX] = color
                    writer.setText('Red Turn')
                    board[tileY][tileX] = None
        

def onMouseMove(x, y):
    pass

def onMouseRelease(x, y):
    pass

def onKeyPress(key):
    pass

def onKeyRelease(key):
    pass

def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        update()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                onMouseMove(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMousePress(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                onMouseRelease(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN:
                onKeyPress(event.key)
            elif event.type == pygame.KEYUP:
                onKeyRelease(event.key)
        clock.tick(FPS)


pygame.init()
mainloop()
