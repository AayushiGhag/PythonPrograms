n = (int(input("Enter a number")))

temp1 = n

while(temp1>0):
    r = temp1%10
    print(r)
    if n%r!=0:
        print("no")
        break
    
        
        

    temp1= temp1//10

if(temp1==0):
    print("YES")
