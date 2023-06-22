n = int(input("Enter a number"))

temp1=temp2=n
count =0
sum=0
while(temp1>0):
    
    count+=1
    
    temp1=temp1//10



while(n!=0):

    sum+=(n%10)**count
    count-=1
    n=n//10

if(sum==temp2):
    print("true")
else:
    print("false")

