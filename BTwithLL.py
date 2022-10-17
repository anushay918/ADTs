freeptr = 0
rootptr = -1

BT = [[-1 for columns in range(3)] for rows in range(10)]
for i in range(10):
    BT[i][2] = i+1
BT[9][2] = -1

def addvalue(value):
    global freeptr, rootptr
    if freeptr == -1:
        print('List is full')
    else:
        BT[freeptr][1] = value
        newnode = freeptr
        freeptr = BT[freeptr][2]
        BT[newnode][2] = -1
        if rootptr == -1:
            rootptr = 0
        else:
            current = rootptr
            placed = False
            while placed == False: 
                if BT[current][1] > value:
                    if BT[current][0] == -1:
                        BT[current][0] = newnode
                        placed = True
                    else:
                        current = BT[current][0]
                else:
                    if BT[current][2] == -1:
                        BT[current][2] = newnode
                        placed = True
                    else:
                        current = BT[current][2]
                        
def searchvalue(value): 
    current = rootptr
    found = False
    while found == False and current != -1:
        if BT[current][1] == value:
            found = True
        elif BT[current][1] < value:
            current = BT[current][2]
        else:
            current = BT[current][0]
    print(current)
    

def traverse(rootptr):
    if rootptr != -1:
        traverse(BT[rootptr][0])
        print(BT[rootptr][1])
        traverse(BT[rootptr][2])
