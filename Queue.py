queue = [-1 for i in range(10)]
 
frontptr = -1 
rearptr = -1
qsize = 0
max = len(queue)
 
def Enq(value):
    global frontptr, rearptr, qsize, queue
    if qsize == max:
        print('overflow')
    else:
        if frontptr == -1:
            frontptr = 0
        if rearptr == len(queue)-1:
            rearptr = 0
        else:
            rearptr = rearptr+1
        queue[rearptr] = value
        qsize = qsize+1
        
def Deq():
    global frontptr, rearptr, queue, qsize
    if qsize == 0:
        print('queue is empty')
    else:
        value = queue[frontptr]
        queue[frontptr] = -1
        qsize = qsize-1
        if frontptr == len(queue)-1:
            frontptr = 0
        else:
            frontptr = frontptr+1
        print(value)
