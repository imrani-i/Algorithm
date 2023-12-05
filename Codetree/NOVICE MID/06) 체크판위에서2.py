

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