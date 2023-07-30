import os

entryDir = os.path.dirname(__file__)
f = open(os.path.join(entryDir, "entrada.txt"), "r")

rock = 'A'
paper = 'B'
scissor = 'C'
lose = 'X'
draw = 'Y'
win = 'Z'

score = 0
for line in f:
    o, e = line.rstrip().lstrip().strip().split(" ")

    if (o == rock):
        if (e == win):
            score += 2
            score += 6
        elif(e == draw):
            score += 1
            score += 3
        else:
            score += 3
            score += 0
    elif (o == paper):
        if (e == win):
            score += 3
            score += 6
        elif(e == draw):
            score += 2
            score += 3
        else:
            score += 1
            score += 0
    else:
        if (e == win):
            score += 1
            score += 6
        elif(e == draw):
            score += 3
            score += 3
        else:
            score += 2
            score += 0

print("final score", score)
