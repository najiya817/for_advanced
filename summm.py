num=12345
sum=0
for i in range(len(str(num))):
    temp=num%10
    num=num//10         #12345%10=1234  5 given to sum
    sum+=temp           #1234%10=123   4 given to sum then 5+4=9
print(sum)              #num%10 removes last number and send the reomved num to sum