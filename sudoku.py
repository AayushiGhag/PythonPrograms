
def display_grid(a):
    for i in range(0,3):
        for j in range(0,3):
            print(a[i][j],end = " ")
        print("\n")


a=[]



for i in range(0,3):
    arr =[]
    for j in range(0,3):
        arr.append(int(input("enter a number")))
    a.append(arr)

display_grid(a)




