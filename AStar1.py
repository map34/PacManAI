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
	global count, BACKLINKS
	OPEN = [initial_state]
	CLOSED = []
	GVALUE = {}
	FVALUE = {}
	GVALUE[Problem.HASHCODE(initial_state)] = 0
	BACKLINKS[Problem.HASHCODE(initial_state)] = -1
	count = 0
	FVALUE[Problem.HASHCODE(initial_state)] = GVALUE[Problem.HASHCODE(initial_state)] + HFunction(initial_state)
	while OPEN != []:
		# Finding a minimum state based on FVALUE
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
			backtrace(n)
			return
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
  global BACKLINKS

  path = []
  while not S == -1:
    path.append(S)
    S = BACKLINKS[Problem.HASHCODE(S)]
  path.reverse()
  print("Solution path: ")
  #for s in path:
  #  print(Problem.DESCRIBE_STATE(s))
  Problem.runPath(path)
  print(str(len(path)) + " solution paths")
  return path    
  

def occurs_in(s1, lst):
  for s2 in lst:
    if Problem.DEEP_EQUALS(s1, s2): return True
  return False

if __name__=='__main__':
  runAStar()


		
	
