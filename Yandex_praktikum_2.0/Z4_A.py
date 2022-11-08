post = int(input())
colors = {}
for _ in range(post):
    color, num = map(int,input().split())
    colors[color] = colors.get(color,0) + num

for i,j in sorted(colors.items(), key=lambda x: x[0]):
    print(i,j)

