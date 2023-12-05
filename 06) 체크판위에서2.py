"""

R * C 크기인 직사각형의 각 칸이 W, B로 표현되어 있습니다.

W는 하얀색으로, B는 검은색으로 칸이 채워져 있는것을 뜻합니다.

왼쪽 상단에서 출발하여 우측 하단으로 이동할 때, 특정 룰을 만족하면서 이동에 성공할 수 있는 경우의 수를 구하는 프로그램을 작성해보세요. 아래가 특정 룰입니다.

1)이동은 항상 점프를 통해서만 가능합니다. 또, 점프 진행시 항상 현재 위치에 적혀있는 색과, 점프한 이후의 칸에 적혀있는 색이 달라야만 합니다.

2)점프 진행시 현재 위치에서 적어도 한칸 이상 오른쪽에 있는 위치이며 동시에 현재 위치에서 적어도 한칸 이상 아래쪽에 있는 위치인 곳으로만 점프가 가능합니다.

3)정확히 시작, 도착 지점을 제외하고 점프하며 도달한 위치가 정확히 2곳 뿐이어야 합니다.

"""

R,C = map(int,input().split())
WB=[]

count=0
for i in range(R):
    WB.append(list(input().split()))
start=WB[0][0]
end=WB[R-1][C-1]
if start==end:
    count=0
else:
    for i in range(1,R-1):
        for j in range(1,C-1):
            if WB[i][j]!=start:
                for k in range(i+1,R-1):
                    for h in range(j+1,C-1):
                        if WB[i][j]!=WB[k][h]:
                            count+=1

print(count)