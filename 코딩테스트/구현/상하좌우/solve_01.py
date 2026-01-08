# if문으로 모두 처리

n = int(input())
move = list(input().split())

def location_detector(n):
    point = [1,1]
    for i in move:
        if i == "L":
            point[1]-=1
            if point[1] < 1:
                point[1] +=1
        elif i == "R":
            point[1]+=1
            if point[1] > n:
                point[1] -=1
        elif i == "U":
            point[0]-=1
            if point[0] < 1:
                point[0] +=1

        else: #i == "D"
            point[0]+=1
            if point[0] > n:
                point[0] -=1

    return point

location_detector(n)