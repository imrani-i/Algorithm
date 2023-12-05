

import sys

N=int(input())
check_point=[]
min_distance=sys.maxsize
for i in range (N):
    check_point.append(list(map(int,input().split())))


for i in range(1,N-1):
    sub_distance=0
    for j in range(N-1):

        if j == i :
            continue
        elif j+1== i :

            sub_distance += abs(check_point[j][0]-check_point[j+2][0])+abs(check_point[j][1]-check_point[j+2][1])

        else:

            sub_distance += abs(check_point[j][0] - check_point[j+1][0]) + abs(check_point[j][1] - check_point[j+1][1])

    min_distance=min(min_distance,sub_distance)

print(min_distance)