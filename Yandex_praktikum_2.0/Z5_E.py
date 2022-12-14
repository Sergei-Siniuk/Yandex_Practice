def slovik(lst: list) -> dict:
    sort_dict = {}
    for index,value in enumerate(lst[1:]):
        sort_dict[int(value)] = sort_dict.setdefault(int(value),index)
    return sort_dict

S = int(input())
A = slovik(input().split())
B = slovik(input().split())
C = slovik(input().split())

break_ = False

for key_A in A:
    if key_A > S:
        continue
    for key_B in B:
        if key_A+key_B > S:
            continue
        if (S - key_A - key_B) in C:
            print(A[key_A],B[key_B],C[S - key_A - key_B])
            break_ = True
            break
    if break_:
        break
else:
    print("-1")