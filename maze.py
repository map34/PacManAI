from tkinter import *
import math
import random
import copy
import FatBoy as agentA
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
                w.create_rectangle(x0, y0, x1,y1, fill="yellow")
            elif mazeList[i][j] == '<':
                w.create_oval(x0+5,y0+5,x1-5,y1-5, fill="red")
            elif mazeList[i][j] == 'M':
                w.create_oval(x0+5,y0+5,x1-5,y1-5, fill="green")
            elif mazeList[i][j] == '0':
                w.create_oval(x0+7,y0+7,x1-7,y1-7, fill="blue")
            x0 += WIDTH/dimx
            x1 += WIDTH/dimx
        y0 += WIDTH/dimx
        y1 += WIDTH/dimx

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
        # if (i % 2 == 1):
        for j in range(DIMY):
            if (maze[i][j] == '0'):
                return i * DIMX + j
        # else:
        #     for j in range(DIMY):
        #         if (maze[i][20 - j] == '0'):
        #             return i * DIMX + j            

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
agentCIndex = 371
agentDIndex = 39
agentEIndex = 399

[agentBX, agentBY] = [int(agentBIndex/DIMX), agentBIndex % DIMX]
[agentCX, agentCY] = [int(agentCIndex/DIMX), agentCIndex % DIMX]
[agentDX, agentDY] = [int(agentDIndex/DIMX), agentDIndex % DIMX]
[agentEX, agentEY] = [int(agentEIndex/DIMX), agentEIndex % DIMX]

previousSpace1 = maze[agentBX][agentBY]
nextSpace1 = ' ' 
previousSpace2 = maze[agentCX][agentCY]
nextSpace2 = ' ' 
previousSpace3 = maze[agentDX][agentDY]
nextSpace3 = ' ' 
previousSpace4 = maze[agentEX][agentEY]
nextSpace4 = ' ' 


enemy1Previous = mazeGUI[agentBX][agentBY]
enemy1PrevState = agentBIndex
enemy1PrevRow = agentBX
enemy1PrevCol = agentBY

enemy2Previous = mazeGUI[agentCX][agentCY]
enemy2PrevState = agentCIndex
enemyPrevRow = agentCX
enemy2PrevCol = agentCY

enemy3Previous = mazeGUI[agentDX][agentDY]
enemy3PrevState = agentDIndex
enemy3PrevRow = agentDX
enemy3PrevCol = agentDY

enemy4Previous = mazeGUI[agentEX][agentEY]
enemy4PrevState = agentEIndex
enemy4PrevRow = agentEX
enemy4PrevCol = agentEY

life = 100

def introduce():
    print("A: "+agentA.agentName() + ': ' + agentA.introduce()+"\n")
    print("B: "+agentB.agentName() + ': ' + agentB.introduce()+"\n")
    print("C: "+agentC.agentName() + ': ' + agentC.introduce()+"\n")
    print("D: "+agentD.agentName() + ': ' + agentD.introduce()+"\n")
    print("E: "+agentE.agentName() + ': ' + agentC.introduce()+"\n")

 
remark = "Hello" 
situationA = {'Character':agentB.agentName() , 'Inside': True, 'Damage': False}
situationB = {'Character':agentA.agentName() , 'Inside': True, 'Damage': False}
situationC = {'Character':agentA.agentName() , 'Inside': True, 'Damage': False}
situationD = {'Character':agentA.agentName() , 'Inside': True, 'Damage': False}
situationE = {'Character':agentA.agentName() , 'Inside': True, 'Damage': False}

turn = 0

def runPath(path, enemy1Path, enemy2Path, enemy3Path, enemy4Path):
    introduce()
    task(path, enemy1Path, enemy2Path, enemy3Path, enemy4Path)
    Button(master, text="Quit", command=quit).pack()
    master.mainloop()

def quit():
    master.quit()
    if (life < 0):
        print("You died. You have failed.")
    else:
        print("You have " + str(life) + " life left! You are victorious!")

def task(path, enemy1Path, enemy2Path, enemy3Path, enemy4Path):
    global enemy1PrevState, enemy1PrevRow, enemy1PrevCol, enemy1Previous
    global enemy2PrevState, enemy2PrevRow, enemy2PrevCol, enemy2Previous
    global enemy3PrevState, enemy3PrevRow, enemy3PrevCol, enemy3Previous
    global enemy4PrevState, enemy4PrevRow, enemy4PrevCol, enemy4Previous
    global remark, situationA, situationB, situationC, situationD, situationE, turn, life

    state = path[task.counter]
    row = int(state/DIMX)
    col = state % DIMX

    #previous
    enemy1PrevRow = int(enemy1PrevState/DIMX)
    enemy1PrevCol = enemy1PrevState % DIMX

    enemy2PrevRow = int(enemy2PrevState/DIMX)
    enemy2PrevCol = enemy2PrevState % DIMX

    enemy3PrevRow = int(enemy3PrevState/DIMX)
    enemy3PrevCol = enemy3PrevState % DIMX

    enemy4PrevRow = int(enemy4PrevState/DIMX)
    enemy4PrevCol = enemy4PrevState % DIMX

    #next
    enemy1State = enemy1Path[task.counter]
    [enemy1Row, enemy1Col] = coordinate(enemy1State)
    enemy1Next = mazeGUI[enemy1Row][enemy1Col]

    enemy2State = enemy2Path[task.counter]
    [enemy2Row, enemy2Col] = coordinate(enemy2State)
    enemy2Next = mazeGUI[enemy2Row][enemy2Col]

    enemy3State = enemy3Path[task.counter]
    [enemy3Row, enemy3Col] = coordinate(enemy3State)
    enemy3Next = mazeGUI[enemy3Row][enemy3Col]

    enemy4State = enemy4Path[task.counter]
    [enemy4Row, enemy4Col] = coordinate(enemy4State)
    enemy4Next = mazeGUI[enemy4Row][enemy4Col]

    if (enemy1State == state):
        life = life - 10
        situationB['Damage'] = True
    elif (enemy2State == state):
        life = life - 10
        situationC['Damage'] = True
    elif (enemy3State == state):
        life = life - 10
        situationD['Damage'] = True
    elif (enemy4State == state):
        life = life - 10
        situationE['Damage'] = True    

    putChar(enemy1PrevRow, enemy1PrevCol, enemy1Previous)
    putChar(enemy2PrevRow, enemy2PrevCol, enemy2Previous)
    putChar(enemy3PrevRow, enemy3PrevCol, enemy3Previous)
    putChar(enemy4PrevRow, enemy4PrevCol, enemy4Previous)
    putChar(row,col,'<')
    putChar(enemy1Row, enemy1Col,'M')
    putChar(enemy2Row, enemy2Col,'M')
    putChar(enemy3Row, enemy3Col,'M')
    putChar(enemy4Row, enemy4Col,'M')

    drawMaze(mazeGUI)
    removeChar(row,col,'p')
    
    putChar(enemy1Row, enemy1Col, enemy1Next)
    putChar(enemy2Row, enemy2Col, enemy2Next)
    putChar(enemy3Row, enemy3Col, enemy3Next)
    putChar(enemy4Row, enemy4Col, enemy4Next)
    task.counter +=1

    enemy1Previous = enemy1Next
    enemy1PrevState = enemy1State
    enemy2Previous = enemy2Next
    enemy2PrevState = enemy2State
    enemy3Previous = enemy3Next
    enemy3PrevState = enemy3State
    enemy4Previous = enemy4Next
    enemy4PrevState = enemy4State


    #Conversation
    if (turn % 5 == 0):
        remarkA = agentA.respond(remark, situationA)    
        print(str(int(turn / 5))+"A: "+agentA.agentName() + ': ' + remarkA+"\n")

        remarkB = agentB.respond(remarkA, situationB)    
        print(str(int(turn / 5))+"B: "+agentB.agentName() + ': ' + remarkB+"\n")

        remarkC = agentC.respond(remarkA, situationC)    
        print(str(int(turn / 5))+"C: "+agentC.agentName() + ': ' + remarkC+"\n")

        remarkD = agentD.respond(remarkA, situationD)    
        print(str(int(turn / 5))+"D: "+agentD.agentName() + ': ' + remarkD+"\n")

        remarkE = agentE.respond(remarkA, situationE)    
        print(str(int(turn / 5))+"E: "+agentE.agentName() + ': ' + remarkE+"\n")

        
        remark = random.choice([remarkB, remarkC, remarkD, remarkE])

    turn += 1

    situationB['Damage'] = False
    situationC['Damage'] = False
    situationD['Damage'] = False
    situationE['Damage'] = False

    master.update()
    if (task.counter == len(path)):
        task.counter = 0
        return
    else:
        master.after(75, lambda: task(path, enemy1Path, enemy2Path, enemy3Path, enemy4Path))
    #print(task.counter)
    #if (task.counter < len(path)-1):
        #task.counter += 1
    
task.counter = 0


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
    if (check != '1' and From != To):

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
    return To

def goal_test(s):

    return s == EXIT

def goal_message(s):
    return "Maze is solved!"
    

# Puts enemy 1 to a place
def putEnemy1(index):
    global previousSpace1, nextSpace1, choose_to_move

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
    
    nextSpace1 = maze[row][col]
    maze[row][col] = 'M'

    [rowOld, colOld] = coordinate(index)
    maze[rowOld][colOld] = previousSpace1

    previousSpace1 = nextSpace1

    return choose_to_move

# once maze is generated, search for all the available open spot in the
#left lower corner section and add indices/coordinates into a list
#use choice(openSpot) to generate a randome spot for ghost to teleport to

openSpot = []
def LowerLeftOpen():
    for i in range(10, 20):
        for j in range(0, 10):
            if maze[i][j] != '1':
                global openSpot
                openSpot.append((i,j))

#lower left section, 9 < row < 20; 0 <= col < 10
def putEnemy2():
    global enemy2PrevState, previousSpace2, nextSpace2, openSpot
    LowerLeftOpen()

    [row, col] = random.choice(openSpot)
    nextSpace2 = maze[row][col]
    maze[row][col] = 'M'

    [rowOld, colOld] = coordinate(enemy2PrevState)
    maze[rowOld][colOld] = previousSpace2

    enemy2PrevState = index([row, col])
    previousSpace2 = nextSpace2

    return index([row, col])


#upper right section, 0 <= row < 10; 9 < col < 20
def putEnemy3(index1):
    global previousSpace3, nextSpace3
    options = []

    
    right = index1+1
    options.append(right)
    left = index1-1
    options.append(left) 
    up = index1 -(DIMY)
    options.append(up)
    down = index1 + (DIMY)
    options.append(down)
    
    choose_to_move = random.choice(options)
    [row, col] = coordinate(choose_to_move)
    
    #out of boudary
    while (row < 0 or row > 9) and (col >19 or col < 10):
        choose_to_move = random.choice(options)
        [row, col] = coordinate(choose_to_move)

    check = maze[row][col]

    if check == '1':
        jumpDir = random.choice(range(4))
        (row, col) = updateRC(row, col, jumpDir)
        while(row < 0 or row > 9) and (col >19 or col < 10):
            jumpDir = random.choice(range(4))
            (row, col) = updateRC(row, col, jumpDir)


    nextSpace3 = maze[row][col]
    maze[row][col] = 'M'

    [rowOld, colOld] = coordinate(index1)
    maze[rowOld][colOld] = previousSpace3

    previousSpace3 = nextSpace3

    return index([row, col])

# Puts enemy 4 to a place
def putEnemy4(index):
    global previousSpace4, nextSpace4, choose_to_move

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
    
    nextSpace4 = maze[row][col]
    maze[row][col] = 'M'

    [rowOld, colOld] = coordinate(index)
    maze[rowOld][colOld] = previousSpace4

    previousSpace4 = nextSpace4

    return choose_to_move

def updateRC(row, col, jumpDir):
    if(dir == 0):
        row = row + 1
    elif(jumpDir == 1):
        row = row - 1 
    elif(jumpDir == 2):
        col = col + 1
    else:
        col = col - 1 
    return (row, col)

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

