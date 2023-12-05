
"""

마라톤 코스는 N개의 체크포인트로 구성되어 있으며,
1번 체크포인트에서 시작해서 모든 체크 포인트를 순서대로 방문한 후 N번 체크포인트에서 마라톤이 끝납니다.
게으른 개발자 A는 막상 대회에 참가하려 하니 귀찮아져서 중간에 있는 체크포인트 한 개를 몰래 건너뛰려 합니다.
단, 1번 체크포인트와 N번 체크포인트를 건너뛰면 티가 많이 나기 때문에 이 두 체크포인트는 건너뛰지 않으려고 합니다.
개발자 A가 체크포인트 한 개를 건너 뛰어서 마라톤을 완주하려고 할 때, 최소 거리를 구하는 프로그램을 작성해보세요.
단, 거리 계산은 택시 거리(Manhattan Distance)를 이용합니다. 택시거리란 |x1-x2|+|y1-y2| 로 계산하는 것을 의미합니다.
또한, 체크 포인트의 좌표는 겹쳐져 주어질 수도 있으며, 이 경우 개발자 A가 체크포인트를 건너뛸 때
그 번호의 체크포인트만 건너뛰게 되며 그 점에 있는 모든 체크포인트를 건너뛰지 않음에 유의합니다.


"""
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