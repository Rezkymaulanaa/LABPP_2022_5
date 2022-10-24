x=0
y=0

def robot():
    global x, y, string
    for i in string:
        if i=="R" or i=="r" :
            x=x+1
            print(x,y)
        elif i=="L" or i=="l":
            x=x-1
            print(x,y)            
        elif i=="U" or i=="u":
            y=y+1
            print(x,y)
        elif i=="D" or i=="d":
            y=y-1
            print(x,y)
    
string=input()
print(x,y)
robot()
while True:
    string=input()

    if string=="end":
        break
    robot()