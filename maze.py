from tkinter import *
import math
import random
import copy
import PacMan as agentA
import IronMan as agentB
import RogerFederer as agentC
import minion as agentD
import marshawnLynch as agentE

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

def putPacMan(row, col):
    mazeGUI[row][col] = '<'

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
            #else :
                #mazeStr += "<"
            #elif maze[i][j] == 'M':
                #mazeStr += 'M'
        mazeStr += "\n"
    print(mazeStr)


def removePacman(row,col):
    mazeGUI[row][col] = 'p'

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


 

def runPath(path):
    task(path)
    Button(master, text="Quit", command=quit).pack()
    master.mainloop()

def quit():
    master.quit()

def task(path):
    state = path[task.counter]
    row = int(state/DIMX)
    col = state % DIMX
    putPacMan(row,col)
    drawMaze(mazeGUI)
    removePacman(row,col)
    task.counter +=1
    master.update()
    if (task.counter == len(path)):
        task.counter = 0
        return
    else:
        master.after(75, lambda: task(path))
    #print(task.counter)
    #if (task.counter < len(path)-1):
        #task.counter += 1
    
task.counter = 0

def task2(path):
    state = path[1]
    row = int(state/DIMX)
    col = state % DIMX
    putPacMan(row,col)
    drawMaze(maze)
    removePacman(row,col)

    #print()
        
task.counter = 0

'''def DESCRIBE_STATE(state):
    row = int(state/ DIMX)
    col = state % DIMX
    putPacMan(row,col)
    master.after(2000,task(path)) 
    removePacman(row,col)
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
    
    if (maze[nTo[0]][nTo[1]] != '1' and From != To):

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

# def ghost():
    # int index = 


################# ENEMIES ###################
agentBIndex = 21
agentCIndex = 39
agentDIndex = 371
agentEIndex = 399

# Puts enemy 1 to a place
def putEnemy1(index):
    options = []
    row = index[0]
    col = index[1]
    #[row, col] = coordinate(index)
    left = [row, col-1]
    options.append(left)
    right = [row, col + 1]
    options.append(right) 
    up = [row + 1, col]
    options.append(up)
    down = [row - 1, col]
    options.append(down)

    choose_to_move = random.choice(options)
    check = maze[choose_to_move[0]][choose_to_move[1]]
    while check == '1' and check == '<' and choose_to_move[0] < DIMX and choose_to_move[1] < DIMY:
        choose_to_move = random.choice(options)
        check = maze[choose_to_move[0]][choose_to_move[1]]
    print(choose_to_move)
    maze[choose_to_move[0]][choose_to_move[1]] = 'M'

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
def h_euclidean(s):
    IndexFrom = coordinate(s)
    IndexTo = coordinate(EXIT)
    rowDiff = IndexTo[0] - IndexFrom[0]
    colDiff = IndexTo[1] - IndexFrom[1]    
    result = math.sqrt(math.pow(rowDiff,2) + math.pow(colDiff,2))
    return result

# counts how many walls inside a state
def h_hammings(s):
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
def h_manhattan(s):
    return EXIT - s
#</OPERATORS>

# return a cordinate of an index
def coordinate(index):
    return [int(index/DIMX), index % DIMX]

def index(coordinate):
    return i * DIMX + j

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
HEURISTICS = {'h_euclidean': h_euclidean, 'h_manhattan':h_manhattan, 'h_hammings':h_hammings}
 #</STAT_VIS>

