import os

entryDir = os.path.dirname(__file__)
f = open(os.path.join(entryDir, "entrada.txt"), "r")

for line in f:
    op, me = line.rstrip().lstrip().strip().split(" ")
