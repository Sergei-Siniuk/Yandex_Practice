with open("input_Z4_B.txt", "r") as file:
    file = file.read().strip().split("\n")

elect = dict()
for i in file:
    i = i.split()
    elect[i[0]] = elect.get(i[0],0) + int(i[1])


for i,j in sorted(elect.items()):
    print(i,j)