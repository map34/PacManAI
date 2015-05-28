from tkinter import *


def getMaze():
    mazeList = []
    fname = "maze.txt"
    with open(fname) as f:
        content = [x.strip('\n') for x in f.readlines()]
        del content[-1]
        for wall in content:
            mazeList.append(list(wall))
    return mazeList

def dim(mazeList):
    return [len(mazeList), len(mazeList[0])]

def createGUI():

    mazeList = getMaze()
    print(dim(mazeList))

    master = Tk()

    w = Canvas(master, width=630, height=630)
    w.pack()

    x0 = 0
    y0 = 0
    x1 = 30
    y1 = 30
    for i in range(21):
        x0 = 0
        x1 = 30
        for j in range (21):
            if mazeList[i][j] == '1':
                w.create_rectangle(x0, y0, x1,y1, fill="blue")
            x0 += 30
            x1 += 30
        y0 += 30
        y1 += 30

    mainloop()

createGUI()

