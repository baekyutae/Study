data= input()

x,y = data[0], data[1]

change = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

x,y = change[x], int(y)


def knight_move(x,y):
    count = 0
    direction = {
    "LeftUP" : (-2,-1),
    "LeftDown": (-2,1),
    "RightUP" : (2,-1),
    "RightDown": (2,1),
    "UpLeft" : (-1,-2),
    "UpRright" : (1,-2),
    "DownLeft" : (-1,2),
    "DownRight" : (1,2)
    }
    for dir in direction:
        move_x, move_y = direction[dir]
        x, y = x + move_x, y + move_y
        #print(x,y)
        if x >0 and x < 9 and y > 0 and y < 9:
            #print(f"{dir} 방향으로 이동 가능")
            count += 1
        x,y = x - move_x, y - move_y # 처음 입력 자리로 복귀

    return count

knight_move(x,y)



       