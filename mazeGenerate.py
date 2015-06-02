from random import shuffle, randrange
import sys

def make_maze(w = 30, h = 30):

    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["10"] * w + ['1'] for _ in range(h)] + [[]]
    hor = [["11"] * w + ['1'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "10"
            if yy == y: ver[y][max(x, xx)] = "00"
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    f = open('maze.txt','w')
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))
        f.write(''.join(a + ['\n'] + b))
        f.write('\n')
    f.close()

make_maze()
