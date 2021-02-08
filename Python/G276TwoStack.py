top1 = top2 = []


def pop1(a):
    global top1
    if top1 == -1:
        return -1
    else:
        val = a[top1]
        top1 -= 1
        return val

# pop element from 2nd stack


def pop2(a):
    global top2
    if top2 == 101:  # size of array is 101, so if stack is empty.
        return -1
    else:
        val = a[top2]
        top2 += 1
        return val

# push element to second stack


def push2(a, x):
    global top1
    global top2
    if top1 < top2-1:
        top2 -= 1
        a[top2] = x

# push element to first stack


def push1(a, x):
    global top1
    global top2
    if top1 < top2-1:
        top1 += 1
        a[top1] = x
