"""

n개의 집이 x = 1에서 x = n까지 순서대로 놓여있고, 각각 Ai명의 사람이 살고 있습니다.
이들은 회의를 위해 n개의 집 중 한 곳에 전부 모이려고 합니다.
적절한 집을 선택하여 모든 사람들의 이동 거리의 합이 최소가 되도록 하는 프로그램을 작성해보세요.

"""
import sys

n=int(input())
x = list(map(int,input().split()))
min_sum = sys.maxsize
for i in range(n):
    min_sub=0

    for j in range(n):
        min_sub+= x[j]*abs(j-i)
    min_sum=min(min_sub,min_sum)

print(min_sum)
