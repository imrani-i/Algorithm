
"""

0 이상의 정수 N을 2진법으로 나타낸 뒤, 그 숫자들 중 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때,
가능한 숫자 N 중 최댓값을 찾는 프로그램을 작성해보세요.

"""

number=list(map(int,str(input())))
sum=0
if number.count(0)==0:
    number[-1]=0

else:
    for i in range(len(number)):
        if number[i]==0:
            number[i]=1
            break
        else :
            continue

for i in range(len(number)):
    if (number[i] == 0):
        continue
    else :
        sum+= 2**(len(number)-i-1)

print(sum)