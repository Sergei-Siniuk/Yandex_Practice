list_S = []
final_list = []
max_count = 0

for _ in range(int(input())):
    list_S.append(input())

for _ in range(int(input())):
    num = input()
    coun = 0
    for j in list_S:
        if set(j).issubset(set(num)):
            coun += 1
    final_list.append((num, coun))
    max_count = max(max_count, coun)

for i in final_list:
    if i[1]==max_count:
        print(i[0])