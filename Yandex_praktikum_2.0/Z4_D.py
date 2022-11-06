partys = []
sumcnt = 0
sum_mest = 0

with open("input_Z4_D.txt", "r") as file:
    file = file.read().strip().split("\n")
    for string, count in zip(file, range(1, len(file) + 1)):
        string = string.split()
        partys.append([count, " ".join(string[:-1]), int(string[-1])])
        sumcnt += int(string[-1])

for string in partys:
    mest = int(string[-1]//(sumcnt/450))
    sum_mest+=mest
    string[-1:] = [mest, (string[-1]%(sumcnt/450))]

if sum_mest<450:
    partys = sorted(partys,key=lambda x: (-x[3],x[0]))
    for i,j  in zip(range(450-sum_mest),partys):
        j[2]+=1

for string in sorted(partys,key=lambda x: x[0]):
    print(string[1], string[2])

