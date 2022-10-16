freeptr = 0
rootptr = -1

BTleft = [-1 for i in range(10)]       
BTright = [-1 for i in range(10)]  
BTdata = ["" for i in range(10)]  

def outputBT():        
    for i in range(10):
        print(BTleft[i], BTdata[i], BTright[i], sep="    ")

def addvalue(value):
    global freeptr, rootptr, BTleft, BTright, BTdata
    if freeptr > 9:
        "Tree is full"
    else:
        BTdata[freeptr] = value
        if rootptr == -1:
            rootptr = 0
        else:
            placed = False
            current = rootptr
            while placed == False and current != -1:
                if value < BTdata[current]:
                    if BTleft[current] == -1:
                        placed = True
                        BTleft[current] = freeptr
                    else:
                        current = BTleft[current]
                else:
                    if BTright[current] == -1:
                        placed = True
                        BTright[current] = freeptr
                    else:
                        current = BTright[current]
        freeptr = freeptr+1

def searchvalue(value):
    current = rootptr
    found = False
    while current != -1 and found == False:
        if BTdata[current] == value:
            found = True
        elif value < BTdata[current]:
            current = BTleft[current]
        else:
            current = BTright[current]
    if found == False:
        print(-1)
    else:
        print(current)
    
def traverse(rootptr):
    if rootptr != -1:
        traverse(BTleft[rootptr])
        print(BTdata[rootptr])
        traverse(BTright[rootptr])
