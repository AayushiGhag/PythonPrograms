import re 

no = input("Enter your credit card number")

def creditCard(no):
    pattern = '*'
    ans = re.sub(r'\d', '*',no)
    print(ans)


creditCard(no)
