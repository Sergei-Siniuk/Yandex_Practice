numbers_of_groups, numbers_of_audiences = map(int, input().split())
number_of_students = list(map(int, input().split()))
number_of_computers = [(j, i - 1) for i, j in zip(map(int, input().split()), range(1, numbers_of_audiences + 1))]
sorted_number_of_computers = sorted(number_of_computers, key=lambda x: x[1])
cabinet_list = []

for i in number_of_students:
    if i > sorted_number_of_computers[-1][1]:
        cabinet_list.append(0)
        continue
    for j in sorted_number_of_computers:
        if i <= j[1]:
            cabinet_list.append(j[0])
            sorted_number_of_computers.remove(j)
            break
    else:
        cabinet_list.append(0)

if len(cabinet_list) == 0 or (len(cabinet_list) == 1 and 0 in cabinet_list):
    print(0)
    print(0)
else:
    print(len(list(filter(lambda x: x != 0, cabinet_list))))
    print(*cabinet_list)
