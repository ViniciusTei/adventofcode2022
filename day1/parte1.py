f = open("entrada.txt", "r")

max = 0
sum = 0
for line in f:
    if (line.isspace()):
        if(max < sum):
            max = sum
        sum = 0
    else:
        num = int(line.rstrip().lstrip().strip())
        sum += num

f.close()

print("Resultado: ", max)

