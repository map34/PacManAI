# Mochamad A. Prananda, Chenshan Yuan 
# CSE 415 HW 3
# Breadth First Search Algorithm Implementation

# ItrBFS.py
# Iterative Breadth-First Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowersOfHanoi.py example file for details.
# Examples of Usage:
# python3 ItrBFS.py TowersOfHanoi
# python3 ItrBFS.py EightPuzzle

import sys

if sys.argv==[''] or len(sys.argv)<2:
  import EightPuzzle as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])


print("\nWelcome to ItrBFS")
COUNT = None
BACKLINKS = {}
path = []

def runDFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  #print("Initial State:")
  #print(Problem.DESCRIBE_STATE(initial_state))
  global COUNT, BACKLINKS
  COUNT = 0
  BACKLINKS = {}
  IterativeBFS(initial_state)
  print(str(COUNT)+" states examined.")
  print(Problem.maze)

def IterativeBFS(initial_state):
  global COUNT, BACKLINKS

  OPEN = [initial_state]
  CLOSED = []
  BACKLINKS[Problem.HASHCODE(initial_state)] = -1

  while OPEN != []:
    S = OPEN[0]

    del OPEN[0]
    CLOSED.append(S);

    if Problem.GOAL_TEST(S):
      if (S == Problem.EXIT):
        backtrace(S)
        Problem.printMaze()
        del OPEN[:]
        del CLOSED[:]
        OPEN.append(S)
        BACKLINKS[Problem.HASHCODE(Problem.EXIT)] = -1
        Problem.EXIT = Problem.getPelletIndex()
        print('next 0 index: ' + str(Problem.EXIT))
        S = OPEN[0]
        del OPEN[0]
        CLOSED.append(S)
        if (Problem.EXIT == -1):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            Problem.runPath(path)


    COUNT += 1
    if (COUNT % 32)==0:
       print("",end="")
       if (COUNT % 128)==0:
         print("COUNT = "+str(COUNT))
         print("len(OPEN)="+str(len(OPEN)))
         print("len(CLOSED)="+str(len(CLOSED)))
    L = []
    for op in Problem.OPERATORS:
      #Optionally uncomment the following when debugging
      #a new problem formulation.
      #print("Trying operator: "+op.name)
      
        
      if op.precond(S):
        new_state = op.state_transf(S)
        
        if not occurs_in(new_state, CLOSED) and not occurs_in(new_state, OPEN):
          L.append(new_state)
          BACKLINKS[Problem.HASHCODE(new_state)] = S
          #Uncomment for debugging:
          #print(Problem.DESCRIBE_STATE(new_state))

    for s2 in L:
      for i in range(len(OPEN)):
        if Problem.DEEP_EQUALS(s2, OPEN[i]):
          del OPEN[i]; break

    OPEN = OPEN + L
    # print('OPEN is: ' + str(OPEN[0]))


def backtrace(S):
  global BACKLINKS, path

  tempPath = []
  while not S == -1:
    [i, j] = Problem.coordinate(S)
    print('S: ' + str(S))
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
  runDFS()

