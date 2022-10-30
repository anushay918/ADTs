stack = []
for i in range(10):
    stack.append(-1)

topptr = -1
max = len(stack)

def addvalue(value):
    global max, topptr, stack
    if topptr == max:
        print('Stack is full sucker')
    else:
        topptr = topptr+1
        stack[topptr] = value
        
def deletevalue():
    global max, topptr, stack
    if topptr == -1:
        print('Stack is empty :( ')
    else:
        value = stack[topptr]
        stack[topptr] = -1
        topptr = topptr-1
        return value
        
def outputstack():
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
