string = input("Enter a roman integer: ")

dict = {'I': 1,'IV': 4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}

number = 0

for i in range(len(string)):
    if i==0:
        number+=dict.get(string[i])
    elif dict.get(string[i-1])<dict.get(string[i]):
        number=dict.get(string[i]) - dict.get(string[i-1])
        
        
        
        
        
    
    else:
        number +=dict.get(string[i])

    
print(number)
