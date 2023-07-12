import os

entryDir = os.path.dirname(__file__)
f = open(os.path.join(entryDir, "entrada.txt"), "r")

# points 
# 1 - rock (A | X)
# 2 - paper (B | Y)
# 3 - scissors (C | Z)
rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
myScore = 0

for line in f:
    if(line.isspace()): break
    op, me = line.strip().rstrip().lstrip().split(" ")
    roundScore = 0
    if (me in rock):
        roundScore += 1
        if (op in rock):
            print("Empate")
            roundScore += 3
        elif (op in paper):
            print("Lose")
        else:
            print("Win")
            roundScore += 6
    elif (me in paper):
        roundScore += 2
        if (op in paper):
            print("Empate")
            roundScore += 3
        elif (op in scissors):
            print("Lose")
        else:
            print("Win")
            roundScore += 6
    else:
        roundScore += 3
        if (op in scissors):
            roundScore += 3
            print("Empate")
        elif (op in rock):
            print("Lose")
        else:
            print("Win")
            roundScore += 6
    myScore += roundScore
print("My score: ", myScore)

        
f.close()
