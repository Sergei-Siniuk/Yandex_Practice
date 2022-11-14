S = int(input())
A = list(map(int, (input()).split()))[1:]
B = list(map(int, (input()).split()))[1:]
C = list(map(int, (input()).split()))[1:]
a = []
b = []
for i in set(A):
    a.append((i, A.index(i)))
for i in set(B):
    b.append((i, B.index(i)))


for i in sorted(a,key=lambda x: x[1]):
    if i[0] > S:
        continue
    break_ = False
    for j in sorted(b,key=lambda x: x[1]):
        if (S - i[0] - j[0]) in set(C):
            print(i[1], j[1], C.index(S - i[0] - j[0]))
            break_ = True
            break
    if break_:
        break
else:
    print("-1")
