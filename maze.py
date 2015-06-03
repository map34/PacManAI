from tkinter import *
import math
import random
import copy
#import PacMan as agentA
#import IronMan as agentB
#import RogerFederer as agentC
#import minion as agentD
#import marshawnLynch as agentE

WIDTH = 630
HEIGHT = 630


# FOR GUI
master = Tk() 
w = Canvas(master, width=WIDTH, height=HEIGHT)


# Get the maze
def getMaze(fname):
    mazeList = []
    with open(fname) as f:
        content = [x.strip('\n') for x in f.readlines()]
        del content[-1]
        for wall in content:
            mazeList.append(list(wall))
    return mazeList

# Get dimension of the maze
def dim(mazeList):
    return [len(mazeList), len(mazeList[0])]

# Draws the maze
def drawMaze(maze):

    dimx = dim(maze)[0]
    dimy = dim(maze)[1]
    mazeList = maze
    w.delete("all") 
    w.pack()
    x0 = 0
    y0 = 0
    x1 = WIDTH/dimx
    y1 = HEIGHT/dimx
    for i in range(dim(mazeList)[0]):
        x0 = 0
        x1 = WIDTH/dimx
        for j in range (dim(mazeList)[1]):
            if mazeList[i][j] == '1':
                w.create_rectangle(x0, y0, x1,y1, fill="blue")
            elif mazeList[i][j] == '<':
                w.create_oval(x0+5,y0+5,x1-5,y1-5, fill="red")
            elif mazeList[i][j] == 'M':
                w.create_oval(x0+5,y0+5,x1-5,y1-5, fill="green")
            elif mazeList[i][j] == '0':
                w.create_oval(x0+7,y0+7,x1-7,y1-7, fill="yellow")
            x0 += WIDTH/dimx
            x1 += WIDTH/dimx
        y0 += WIDTH/dimx
        y1 += WIDTH/dimx

'''def runGUI():
    drawMaze(maze)
    
    def task():
        createGUI("maze.txt",w)
        master.after(500, task2)

    def task2():
        createGUI("maze1.txt",w)
        master.after(500, task)

    master.after(500, task)
    master.mainloop()
'''

def putChar(row, col,char):
    mazeGUI[row][col] = char

def printMaze():
    mazeStr = ""
    for i in range(DIMX+1):
        for j in range(DIMY+1):
            if maze[i][j] == '0':
                mazeStr += " "
            elif maze[i][j] == '1':
                mazeStr += "#"
            elif maze[i][j] == 'M':
               mazeStr += "M"
            elif maze[i][j] == '<':
                mazeStr += "<"
            else:
                mazeStr += "."
            #elif maze[i][j] == 'M':
                #mazeStr += 'M'
        mazeStr += "\n"
    print(mazeStr)


def removeChar(row,col,char):
    mazeGUI[row][col] = char

def getPelletIndex():
    for i in range(DIMX):
        for j in range(DIMY):
            if (maze[i][j] == '0'):
                return i * DIMX + j

    return -1
########################## BACK END ############################


maze = getMaze("maze.txt")
mazeGUI = getMaze("maze.txt")
# INITIAL STATES
DIMX = dim(maze)[0]-1
DIMY = dim(maze)[1]-1
# START = DIMX + 1
# Start at the center 
START = 381 - 160 + 10 
[x, y] = [int(START/DIMX), START % DIMX]
maze[x][y] = ' '
# EXIT = DIMX*DIMY - 1
EXIT = getPelletIndex()

################# ENEMIES ###################
agentBIndex = 81
agentCIndex = 39
agentDIndex = 371
agentEIndex = 399

[agentBX, agentBY] = [int(agentBIndex/DIMX), agentBIndex % DIMX]

previousSpace = maze[agentBX][agentBY]
nextSpace = '' 


enemyPrevious = mazeGUI[agentBX][agentBY]
enemy1PrevState = agentBIndex
enemy1PrevRow = agentBX
enemy1PrevCol = agentBY


 

def runPath(path, enemy1Path):
    task(path, enemy1Path)
    Button(master, text="Quit", command=quit).pack()
    master.mainloop()

def quit():
    master.quit()

def task(path, enemy1Path):
    global enemy1PrevState, enemy1PrevRow, enemy1PrevCol, enemyPrevious
    state = path[task.counter]
    row = int(state/DIMX)
    col = state % DIMX

    #previous
    enemy1PrevRow = int(enemy1PrevState/DIMX)
    enemy1PrevCol = enemy1PrevState % DIMX

    
    #next
    enemy1State = enemy1Path[task.counter]
    [enemy1Row, enemy1Col] = coordinate(enemy1State)

    enemyNext = mazeGUI[enemy1Row][enemy1Col]

    putChar(enemy1PrevRow, enemy1PrevCol, enemyPrevious)
    putChar(row,col,'<')
    putChar(enemy1Row, enemy1Col,'M')

    drawMaze(mazeGUI)
    removeChar(row,col,'p')
    #removeChar(enemy1Row, enemy1Col,enemyNext)
    putChar(enemy1Row, enemy1Col, enemyNext)
    task.counter +=1

    enemyPrevious = enemyNext
    enemy1PrevState = enemy1State
    master.update()
    if (task.counter == len(path)):
        task.counter = 0
        return
    else:
        master.after(75, lambda: task(path, enemy1Path))
    #print(task.counter)
    #if (task.counter < len(path)-1):
        #task.counter += 1
    
task.counter = 0

def task2(path):
    state = path[1]
    row = int(state/DIMX)
    col = state % DIMX
    putChar(row,col)
    drawMaze(maze)
    removeChar(row,col)

    #print()
        
task.counter = 0

'''def DESCRIBE_STATE(state):
    row = int(state/ DIMX)
    col = state % DIMX
    putChar(row,col)
    master.after(2000,task(path)) 
    removeChar(row,col)
'''
def DEEP_EQUALS(s1,s2):
    return s1 == s2

def HASHCODE(s):
    return "{" +str(s) + "}"  

def copy_state(s):
    temp = copy.deepcopy(s)
    return temp

def can_move(s, From, To):
    From = copy_state(s)
    nFrom = (int(From/ DIMX), From % DIMX)
    nTo = (int(To / DIMX), To % DIMX)

    #print(nFrom)
    #print(nTo)
    check = maze[nTo[0]][nTo[1]]
    if (check != '1' and check != 'M' and From != To):

        if nFrom[0] == nTo[0] and nFrom[1] == nTo[1]-1 :
            return True
        elif nFrom[0] == nTo[0] and nFrom[1] == nTo[1]+1 :
            return True
        elif nFrom[1] == nTo[1] and nFrom[0] == nTo[0]-1 :
            return True
        elif nFrom[1] == nTo[1] and nFrom[0] == nTo[0]+1 :
            return True
    else: 
        return False

def move(s,From,To):
    # print('s is : ' + str(s))
    # print('From is : ' + str(From))
    # print('To is : ' + str(To) + '\n')
    # [i, j] = coordinate(To)
    # print('To ' + str(To))
    # maze[i][j] = ' '
    return To

def goal_test(s):
    # global EXIT
    # if (s == EXIT):
    #     print("here")
    #     printMaze()
    #     EXIT = getPelletIndex();
    #     if (EXIT == -1):
    #         return True
    # return False
    # print(maze[1])
    return s == EXIT

def goal_message(s):
    return "Maze is solved!"

# Top Right corner = 39
# Top Left corner = 21
# Bottom Right corner = 399
# Bottom Left corner = 371

    


# Puts enemy 1 to a place
def putEnemy1(index):
    global previousSpace, nextSpace, choose_to_move

    options = []

    #[row, col] = coordinate(index)
    right = index+1
    options.append(right)
    left = index-1
    options.append(left) 
    up = index -(DIMY)
    options.append(up)
    down = index + (DIMY)
    options.append(down)

    #print(options)
    choose_to_move = random.choice(options)
    [row, col] = coordinate(choose_to_move)
    check = maze[row][col]
    while check == '1':
        choose_to_move = random.choice(options)
        [row, col] = coordinate(choose_to_move)
        check = maze[row][col]
    
    nextSpace = maze[row][col]
    maze[row][col] = 'M'


    [rowOld, colOld] = coordinate(index)
    maze[rowOld][colOld] = previousSpace

    previousSpace = nextSpace

    return choose_to_move


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

INITIAL_STATE = START
CREATE_INITIAL_STATE = lambda: INITIAL_STATE
DUMMY_STATE = []

#<OPERATORS>
#Creates list of operators
move_combination = []
for i in range(DIMX*DIMY): # Dimension = size of maze

        right = (i, i+1)
        move_combination.append(right)

        left = (i, i-1)
        move_combination.append(left)

        up = (i , (int(i/DIMX)%DIMX)-DIMX)
        move_combination.append(up)

        down = (i, (int(i/DIMX)%DIMX)+DIMX)
        move_combination.append(down)

# p and q stands for the index of in the list
OPERATORS = [Operator("Move "+str(p)+" to "+str(q),
    lambda s,p=p,q=q: can_move(s,p,q),
    # The default value construct is needed
    # here to capture the values of p&q separately
    # in each iteration of the list comp. iteration.
    lambda s,p=p,q=q: move(s,p,q))
    for (p,q) in move_combination]

# the 2d distance between current position to s
def h_euclidean(s,loc):
    IndexFrom = coordinate(s)
    IndexTo = coordinate(EXIT)
    rowDiff = IndexTo[0] - IndexFrom[0]
    colDiff = IndexTo[1] - IndexFrom[1]    
    result = math.sqrt(math.pow(rowDiff,2) + math.pow(colDiff,2))
    return result

# counts how many walls inside a state
def h_hammings(s, loc):
    r = int(s / DIMX)
    c = s % DIMX
    sum = 0
    if (maze[r][c+1] == '1'):
        sum += 1
    if (maze[r][c-1] == '1'):
        sum += 1
    if (maze[r-1][c] == '1'):
        sum += 1
    if (maze[r+1][c] == '1' ):
        sum += 1
    return sum

# dx + dy between current position to EXIT
def h_manhattan(s, loc):
    return EXIT - s

# distance between exit and ghost
def h_ghost(s, loc):
    return  -math.fabs(s - loc)
#</OPERATORS>

# return a cordinate of an index
def coordinate(index):
    return [int(index/DIMX), index % DIMX]

def index(coordinate):
    return coordinate[0] * DIMX + coordinate[1]

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
HEURISTICS = {'h_euclidean': h_euclidean, 'h_manhattan':h_manhattan, 'h_hammings':h_hammings, 'h_ghost':h_ghost}
 #</STAT_VIS>

