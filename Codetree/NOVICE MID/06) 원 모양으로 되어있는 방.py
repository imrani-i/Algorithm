

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


