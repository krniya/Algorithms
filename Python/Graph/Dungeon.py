from queue import Queue
r = 7
c = 5

m = [['S','.','.','#','.','.','.'],
     ['.','#','.','.','.','#','.'],
     ['.','#','.','.','.','.','.'],
     ['.','.','#','#','.','.','.'],
     ['#','.','#','E','.','#','.']]

sr = sc = 0
rq = Queue(maxsize= r*c)
cq = Queue(maxsize= r*c)
move_count = 0
nodes_left = 1
nodes_next = 0
reached = False
visited = [ [False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False]
        ]
dr = [-1,1,0,0]
dc = [0,0,1,-1]

def solve():
    rq.put(sr)
    cq.put(sc)
    visited[sr][sc]= True
    while rq.qsize > 0:
        r = rq.get()
        c = cq.get()
        if m[r][c] == 'E':
            reached = True

