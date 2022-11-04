number_of_folders=int(input())

folders=list(map(int,input().split()))
max=0
summa=0
for i in folders:
    summa+=i
    if i>max:
        max=i

print(summa-max)