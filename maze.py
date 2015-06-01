from tkinter import *
import math
import copy

WIDTH = 630
HEIGHT = 630


# FOR GUI
master = Tk() 
w = Canvas(master, width=WIDTH, height=HEIGHT)



def getMaze(fname):
    mazeList = []
    with open(fname) as f:
        content = [x.strip('\n') for x in f.readlines()]
        del content[-1]
        for wall in content:
            mazeList.append(list(wall))
    return mazeList

def dim(mazeList):
    return [len(mazeList), len(mazeList[0])]


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


def putPacman(row, col):
    maze[row][col] = '<'

def printMaze():
    mazeStr = ""
    for i in range(DIMX+1):
        for j in range(DIMY+1):
            if maze[i][j] == '0':
                mazeStr += " "
            elif maze[i][j] == '1':
                mazeStr += "#"
            else:
                mazeStr += "<"
        mazeStr += "\n"
    print(mazeStr)

def removePacman(row,col):
    maze[row][col] = 'p'

def getPelletIndex():
    for i in range(DIMX):
        for j in range(DIMY):
            if (maze[i][j] == '0'):
                return i * DIMX + j * DIMY


########################## BACK END ############################


maze = getMaze("maze1.txt")
# INITIAL STATES
DIMX = dim(maze)[0]-1
DIMY = dim(maze)[1]-1
START = DIMX + 1
EXIT = DIMX*DIMY - 1
<<<<<<< HEAD
# EXIT = getPelletIndex()
=======

>>>>>>> parent of 4b927f4... New files

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
    putPacman(row,col)
    drawMaze(maze)
    removePacman(row,col)
    #printMaze()
    task.counter +=1
    master.update()
    if (task.counter == len(path)):
        task.counter = 0
        return
    else:
        master.after(500, lambda: task(path))
    #print(task.counter)
    #if (task.counter < len(path)-1):
        #task.counter += 1
    
task.counter = 0

<<<<<<< HEAD
=======
def task2(path):
    state = path[1]
    row = int(state/DIMX)
    col = state % DIMX
    putPacMan(row,col)
    drawMaze(maze)
    removePacman(row,col)

    #print()
    

        
task.counter = 0

>>>>>>> parent of 4b927f4... New files
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
    logic = False
    if (maze[nTo[0]][nTo[1]] == '0' and From != To):
        if nFrom[0] == nTo[0] and nFrom[1] == nTo[1]-1 :
            logic = True
        elif nFrom[0] == nTo[0] and nFrom[1] == nTo[1]+1 :
            logic = True
        elif nFrom[1] == nTo[1] and nFrom[0] == nTo[0]-1 :
            logic = True
        elif nFrom[1] == nTo[1] and nFrom[0] == nTo[0]+1 :
            logic = True
    else: 
        logic = False

    return logic

def move(s,From,To):
    return To

def goal_test(s):
    # for i in range(DIMX):
    #     for j in range(DIMY):
    #         if (maze[i][j] == '0'):
    #             return False

    # return True
    #printMaze()
    return s == EXIT

def goal_message(s):
    return "Maze is solved!"



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
    if (maze.is_wall(r,c,1,0)):
        sum += 1
    if (maze.is_wall(r,c,0,1)):
        sum += 1
    if (maze.is_wall(r,c,-1,0)):
        sum += 1
    if (maze.is_wall(r,c,0,-1)):
        sum += 1
    return sum

# dx + dy between current position to EXIT
def h_manhattan(s):
    return EXIT - s
#</OPERATORS>

# return a cordinate of an index
def coordinate(index):
	return [int(index/DIMX), index % DIMX]

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
HEURISTICS = {'h_euclidean': h_euclidean, 'h_manhattan':h_manhattan, 'h_hammings':h_hammings}
 #</STAT_VIS>

