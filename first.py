n = int(input("enter the number of guests : "))

arr =[]
a=[]

total_cost = 0.00
for i in range(0,n):
    age = int(input("enter the age : "))

    if age>0 and age <= 2:
        total_cost +=0.00
        arr.append(age)
        a.append(0.00)
    elif age>2 and age<=12:
        total_cost+=14.00
        arr.append(age)
        a.append(14.00)
    elif age>=65:
        total_cost+=18.00
        arr.append(age)
        a.append(18.00)
    elif age >12 and age <65:
        total_cost+=23.00
        arr.append(age)
        a.append(23.00)
    else:
        print("Your input for the age is invalid.\nPlease put a correct age.")
        i-=1


        
print("*********************Invoice*********************\n")
print("         The no of guests are: ",n)

print("         No.of guests         Age            Cost pp\n")

for i in range(n):
    print("         ",i+1,"                  ",arr[i],"             ",a[i],"\n")


format_cost = "{:.2f}".format(total_cost)


print("*************************************************\n")
print("Your total cost will be:",format_cost,"\n")
    
    
print("****************THANK YOU**********************")

