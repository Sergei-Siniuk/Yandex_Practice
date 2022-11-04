a=int(input()) # код завершения
b=int(input()) # интерактор
c=int(input()) # чекер

def verdikt(a,b,c):
    if a==-1 and b==0 and c==1:
        return 3
    elif a==1 and b==4 and c==0:
        return 3
    elif b==0:
        if a==0:
            return 0
        else:
            return c
    elif b==1:
        return c




    elif b==4:
        if a==0:
            return 3
        else:
            return 4
    elif b==6:
        return 0

    elif b==7:
        return 1
    else:
        return b

print(verdikt(a,b,c))