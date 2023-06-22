import math

triangle=[]

for i in range(3):
    arr=[]
    print("Enter the points for ",i+1," triangle")
    for j in range(2):
        arr.append(int(input()))
    triangle.append(arr)



def eucledian_distance(point1,point2):
    
    sum=(point1-point2)**2 
    
    return sum

distance1 = math.sqrt((arr[0][0]-arr[1][0])**2 + (arr[0][1]-arr[1][1])**2)
distance2 = math.sqrt((arr[0][0]-arr[2][0])**2 + (arr[0][1]-arr[2][1])**2)
distance3 = math.sqrt((arr[1][0]-arr[2][0])**2 + (arr[1][1]-arr[2][1])**2)

perimeter = distance1+distance2+distance3

print("The perimeter of a triangle : ",perimeter)


