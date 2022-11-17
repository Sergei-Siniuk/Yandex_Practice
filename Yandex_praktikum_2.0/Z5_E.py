S = int(input())
A = list(map(int, (input()).split()))[1:]
B = list(map(int, (input()).split()))[1:]
C = list(map(int, (input()).split()))[1:]

break_ = False
iter = 0


for i_index, i_value in enumerate(A):
    if i_value>S:
        continue
    for j_index, j_value in enumerate(B):
        if i_value + j_value > S:
            continue
        iter+=1
        if (S - i_value - j_value) in set(C):
            print(i_index, j_index, C.index(S - i_value - j_value))
            break_ = True
            break
    if break_:
        break
else:
    print("-1")
print(iter)