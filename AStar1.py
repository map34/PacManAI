# AStar.py
# Mochamad Prananda, Chenshan Yuan
# Ver 0.1, April 20, 2015.
# Iterative A-Star Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowersOfHanoi.py example file for details.
import sys


if sys.argv==[''] or len(sys.argv) < 2:
    import EightPuzzle as Problem
elif len(sys.argv)== 3:
    import importlib
    Problem = importlib.import_module(sys.argv[1])
    HFunction = Problem.HEURISTICS[sys.argv[2]]
    #Puzzle = importlib.import_module(sys.argv[3].replace(".py","")) 
    
path = []

print("Welcome to AStar Algorithm!\n")
COUNT = None
BACKLINKS = {}

def runAStar():
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("INITIAL STATE: ")
    #print(Problem.DESCRIBE_STATE(initial_state))
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    AStar(initial_state)
    print(str(count) + " states examined.")

def AStar(initial_state):
    global count, BACKLINKS, enemy1State
    OPEN = [initial_state]
    enemy1State = Problem.coordinate(Problem.agentBIndex)

    CLOSED = []
    GVALUE = {}
    FVALUE = {}
    GVALUE[Problem.HASHCODE(initial_state)] = 0
    BACKLINKS[Problem.HASHCODE(initial_state)] = -1
    count = 0
    FVALUE[Problem.HASHCODE(initial_state)] = GVALUE[Problem.HASHCODE(initial_state)] + HFunction(initial_state)
    while OPEN != []:
        # Finding a minimum state based on FVALUE
        # move ghost
        enemy1State = Problem.putEnemy1(enemy1State)
        #Problem.printMaze()
        minimumState = initial_state
        for state in OPEN:
            minimumState = state
        index = len(OPEN) - 1
        for i in range(len(OPEN)):
            if FVALUE[Problem.HASHCODE(OPEN[i])] < FVALUE[Problem.HASHCODE(minimumState)]:
                minimumState = OPEN[i]
                index = i

        n = OPEN[index]
        CLOSED.append(n)

        # Ending state
        if Problem.GOAL_TEST(n):
            if n == Problem.EXIT:
                backtrace(n)
                Problem.printMaze()
                new_in_state= Problem.EXIT
                Problem.EXIT = Problem.getPelletIndex()
                # New solving
                OPEN = [new_in_state]
                CLOSED = []
                GVALUE = {}
                FVALUE = {}
                GVALUE[Problem.HASHCODE(new_in_state)] = 0
                BACKLINKS[Problem.HASHCODE(new_in_state)] = -1
                FVALUE[Problem.HASHCODE(new_in_state)] = GVALUE[Problem.HASHCODE(new_in_state)] + HFunction(new_in_state)
                # Find minimum
                minimumState = new_in_state
                for state in OPEN:
                    minimumState = state
                index = len(OPEN) - 1
                for i in range(len(OPEN)):
                    if FVALUE[Problem.HASHCODE(OPEN[i])] < FVALUE[Problem.HASHCODE(minimumState)]:
                        minimumState = OPEN[i]
                        index = i

                n = OPEN[index]
                CLOSED.append(n)
                if (Problem.EXIT == -1):
                    print(Problem.GOAL_MESSAGE_FUNCTION(n)) 
                    Problem.runPath(path)


        # count outputting
        count+= 1
        if (count % 32)==0:
            print("")
            if (count % 128)==0:
                print("count = "+str(count))
                print("len(OPEN)="+str(len(OPEN)))
                print("len(CLOSED)="+str(len(CLOSED)))

            # Eliminate and choose in possibilities
        for op in Problem.OPERATORS:
            if op.precond(n):
                newState = op.state_transf(n)
                if  occurs_in(newState, CLOSED):
                    continue
                gTemp = GVALUE[Problem.HASHCODE(n)] + 1
                hTemp = HFunction(newState)


                if not occurs_in(newState, OPEN) or gTemp < GVALUE[Problem.HASHCODE(newState)]:
                    GVALUE[Problem.HASHCODE(newState)] = gTemp
                    FVALUE[Problem.HASHCODE(newState)] = gTemp + hTemp
                    if not occurs_in(newState, OPEN):
                        OPEN.append(newState)
                    BACKLINKS[Problem.HASHCODE(newState)] = n


            # Deleting min
        del OPEN[index]
        del FVALUE[Problem.HASHCODE(n)]
        del GVALUE[Problem.HASHCODE(n)]




def backtrace(S):
    global BACKLINKS, path
    tempPath = []
    while not S == -1:
        [i, j] = Problem.coordinate(S)
        Problem.maze[i][j] = ' '
        tempPath.append(S)
        S = BACKLINKS[Problem.HASHCODE(S)]
    tempPath.reverse()
    print("Solution path: ")
    #for s in path:
    #  print(Problem.DESCRIBE_STATE(s))
    print(str(len(tempPath)) + " solution paths")
    print(tempPath)
    # Problem.runPath(path)
    for i in range(len(tempPath)):
        path.append(tempPath[i])
    # path.append(tempPath)
    return tempPath     
        
      
def occurs_in(s1, lst):
    for s2 in lst:
        if Problem.DEEP_EQUALS(s1, s2): return True
    return False
  
if __name__=='__main__':
    runAStar()
  
  
                  
          
