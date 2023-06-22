n = int(input("enter the no of teams: "))




for i in range(n+1):
    teams = [[] for i in range(i)]


def match():
    for i in range(len(teams)):
        for m in range(i+1,len(teams)):
            print("*******This is the match between ",i,"and ",m)
            win = int(input("who is the winner?"))
            if(win == i):
                teams[i].append(2)
            elif win == m:
                teams[m].append(2)
            else:
                teams[i].append(1)
                teams[m].append(1)
    




print(teams)





