freeptr = 0
startptr = -1

LL = [[-1 for coloumns in range(2)] for rows in range(10)]
for i in range(10):
    LL[i][1] = i+1
LL[9][1] = -1

def outputlist():
    for i in range(10):
        print(LL[i][0], LL[i][1], sep="  ")

def addvalue(value):
    global LL, freeptr, startptr
    if freeptr == -1:
        print('List is full')
    else:
        LL[freeptr][0] = value
        newnode = freeptr
        freeptr = LL[freeptr][1]
        LL[newnode][1] = -1
        previousnode = -1
        current = startptr
        while current != -1 and LL[current][0] < value:
            previousnode = current
            current = LL[current][1]
        if previousnode == -1:
            LL[newnode][1] = startptr
            startptr = newnode
            
        else:
            LL[previousnode][1] = newnode
            LL[newnode][1] = current
            

def deletevalue(value):
    global LL, freeptr, startptr
    if startptr == -1:
        print('List is empty')
    else:
        current = startptr
        previousnode = -1
        while current != -1 and LL[current][0] != value:
            previousnode = current
            current = LL[current][1]
        if current == -1:
            print("Value not found")
        else:
            if current == startptr:
                startptr = LL[current][1]
            else:
                LL[previousnode][1] = LL[current][1]
            LL[current][1] = freeptr
            freeptr = current
            LL[current][0] = -1
            
def searchvalue(value):
    current = startptr
    while current != -1 and LL[current][0] != value:
        current = LL[current][1]
    print(current)
    
def traverse():
    current = startptr
    while current != -1:
        print(LL[current][0])
        current = LL[current][1]
