
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
