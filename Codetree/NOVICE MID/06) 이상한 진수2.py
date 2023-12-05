

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