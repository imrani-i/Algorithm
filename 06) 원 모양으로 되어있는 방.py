"""
원 모양으로 되어있는 N개의 방이 있고, 방은 1부터 N까지 시계 반대방향으로 번호가 매겨져 있습니다.
각 방에는 이웃한 두 개의 방으로 통하는 문이있습니다. 사람들은 무조건 시계 반대방향으로만 이동해야 합니다.

각자 방에 몇 명이 사람이 들어가야하는지 주어지며, 모든 사람이 같은 방에서 시작한다고 합니다.
어떤 방에서 시작해야 각 방에 정해진 인원이 들어가는 데까지의 거리의 합을 최소화 할 수 있는지를 계산하는 프로그램을 작성해보세요.

"""

import sys

N=int(input())
people=[]
min_distance=sys.maxsize
for i in range(N):
    people.append(int(input()))

for i in range(N):
    sub_distance=0
    j=i+1
    gap=1
    while(1):
        if j == N :
            j=0
        if j==i:
            break
        sub_distance+= gap*people[j]
        j+=1
        gap+=1


    min_distance=min(min_distance,sub_distance)

print(min_distance)


