
n=int(input())
number=[]
for i in range(n):
    number.append(int(input()))
length=len(str(max(number)))

max_num = -1
def check(a,b,c):
    sum=a+b+c
    for l in range(length):
        sub_sum = a%10 + b%10 + c%10
        if sub_sum >= 10 :
            return -1
        else :
            a=a//10
            b=b//10
            c=c//10
    return sum



for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            max_num=max(max_num, (check(number[i],number[j],number[k])))

print(max_num)