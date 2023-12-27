N,M=map(int,input().split())

arr = [list(map(str, input().strip())) for _ in range(N)] #strip(한글자씩 끊어서)

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

def check(arr):
    dxs, dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt=0
    for i in range(N):
        for j in range(M):

            if arr[i][j]!='L':
                continue

            for dx,dy in zip(dxs,dys):
                if in_range(i+dx,j+dy)==False:
                    continue

                ix,jy=i+dx,j+dy

                if in_range(ix+dx,jy+dy)==False:
                    continue

                if arr[ix][jy]=='E' and arr[ix+dx][jy+dy]=='E':
                    cnt+=1

    print(cnt)

check(arr)

/***

1) 완전 탐색 , 이중포문 
2) 'L'을 기준으로 8방향으로 체크
3) 해당 방향에서 인덱스 에러가 나지 않으면, 한 번 더 해당 방향으로 인덱스 체크 ('L'을 기준으로 하여 같은 방향으로 두번 이동 했을 때 인덱스 오류가 없어야함) -> 배열 범위 안에 없을 시 continue
4) 앞에서 선택된 인덱스 값이 둘 다 'E'로 동일하면 cnt 값 증가 

***/
