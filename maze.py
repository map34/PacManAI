def getMaze():
    mazeList = []
    fname = "maze.txt"
    with open(fname) as f:
        content = [x.strip('\n') for x in f.readlines()]
        del content[-1]
        for wall in content:
            mazeList.append(list(wall))
    return mazeList

getMaze()
