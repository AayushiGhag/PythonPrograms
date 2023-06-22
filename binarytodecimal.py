n = int(input())

sum=0
count=-1
while(n>0):
    count+=1 #0
    sum += (2**count)*(n%10) #0+0
    n=n//10




print(sum)