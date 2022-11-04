# d = int(input())
# X_x, X_y = map(int, input().split())
def treu(d, X_x, X_y):
    if X_x >= 0 and X_y >= 0 and X_x + X_y <= d:
        return (0)
    elif X_x<=d/2 and X_y<=d/2:
        return (1)
    elif X_x >= d / 2 and X_y <= d / 2 or X_y == d and X_x == d or X_x > 0 and X_y > 0 and X_y == X_x:
        return (2)
    else:
        return (3)

# print(treu(d,X_x,X_y))

def rastoianie(x,y,d):
    if x>0 and y>0 and x+y<=d:
        print(0)
    else:
        print(f"Расстояние до точки A={x**2+y**2} - 1")
        print(f"Расстояние до точки B={(x-d)**2+y**2} - 2")
        print(f"Расстояние до точки C={x**2+(y-d)**2} - 3")

rastoianie(1,1,5)
rastoianie(4,4,4)

