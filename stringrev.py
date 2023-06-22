s = input("Enter a string:  ")

st =""
rev_str = s[::-1]

dict = {'a':0,'e':1,'i':2,'o':3,'u':4}

for i in rev_str:
    if i in dict:
        st+= str(dict.get(i))
    else:
        st+=i


st+='aca'

print(st)

