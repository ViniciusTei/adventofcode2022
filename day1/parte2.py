f = open("entrada.txt", "r")

sum = 0
list = []

for line in f:
    if (line.isspace()):
        list.append(sum)
        sum = 0
    else:
        num = line.rstrip().lstrip().strip()
        sum += int(line.rstrip())
list.sort(reverse=True)

sum = 0

for x in list[0:3]:
    sum += x

print("resultado", sum)

f.close()

