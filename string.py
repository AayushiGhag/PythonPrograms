decimal_number = int(input("enter a number"))
binary_number =""

while(decimal_number>0):
    binary_number = str(decimal_number%2) + binary_number
    decimal_number= decimal_number//2

print(binary_number)
