plan=list(map(int,input().split()))
index_shop=[]
index_house=[]
list_min_distance=[]

for index,value in enumerate(plan):
    if value==1:
        index_house.append(index)
    elif value==2:
        index_shop.append((index))

for house in index_house:
    min_distance = 10
    for shop in index_shop:
        distance=abs(house-shop)
        if distance<min_distance:
            min_distance=distance
    list_min_distance.append(min_distance)

print(max(list_min_distance))

