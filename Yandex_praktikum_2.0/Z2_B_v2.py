plan=list(map(int,input().split()))
shops_distance_l=-20
shops_distance_r = 20
long_distance = 0

list_distance_hous=[0]*10
for i in range(1,len(plan)+1):
    if plan[i-1]==2:
        shops_distance_l=i
    if plan[i-1]==1:
        list_distance_hous[i-1]=i-shops_distance_l


for i in range(len(plan),0,-1):
    if plan[i-1]==2:
        shops_distance_r=i
    if plan[i-1]==1:
        min_dist=min(shops_distance_r-i,list_distance_hous[i-1])
        long_distance=max(min_dist,long_distance)


print(long_distance)